#!/usr/bin/env python3
"""
FitLife Blog Backend API Test Suite
Tests all backend API endpoints comprehensively
"""

import requests
import json
import sys
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/app/frontend/.env')

# Get backend URL from environment
BACKEND_URL = os.getenv('REACT_APP_BACKEND_URL', 'https://fit-life-2.preview.emergentagent.com')
API_BASE = f"{BACKEND_URL}/api"

class FitLifeAPITester:
    def __init__(self):
        self.base_url = API_BASE
        self.test_results = {
            'passed': 0,
            'failed': 0,
            'errors': []
        }
        
    def log_result(self, test_name, success, message=""):
        """Log test result"""
        if success:
            self.test_results['passed'] += 1
            print(f"✅ {test_name}: PASSED")
        else:
            self.test_results['failed'] += 1
            self.test_results['errors'].append(f"{test_name}: {message}")
            print(f"❌ {test_name}: FAILED - {message}")
    
    def test_health_check(self):
        """Test API health check"""
        try:
            response = requests.get(f"{self.base_url}/", timeout=10)
            if response.status_code == 200:
                data = response.json()
                if "FitLife Blog API is running" in data.get('message', ''):
                    self.log_result("Health Check", True)
                    return True
                else:
                    self.log_result("Health Check", False, f"Unexpected response: {data}")
            else:
                self.log_result("Health Check", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Health Check", False, f"Connection error: {str(e)}")
        return False
    
    def test_get_all_articles(self):
        """Test GET /api/articles - Should return all articles"""
        try:
            response = requests.get(f"{self.base_url}/articles", timeout=10)
            if response.status_code == 200:
                articles = response.json()
                if isinstance(articles, list):
                    print(f"   Found {len(articles)} articles")
                    if len(articles) >= 8:  # Should have 8 seeded articles
                        # Verify article structure
                        if articles and all(key in articles[0] for key in ['id', 'title', 'category', 'author']):
                            self.log_result("Get All Articles", True)
                            return articles
                        else:
                            self.log_result("Get All Articles", False, "Invalid article structure")
                    else:
                        self.log_result("Get All Articles", False, f"Expected 8+ articles, got {len(articles)}")
                else:
                    self.log_result("Get All Articles", False, "Response is not a list")
            else:
                self.log_result("Get All Articles", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get All Articles", False, f"Error: {str(e)}")
        return []
    
    def test_get_articles_by_category(self):
        """Test GET /api/articles?category=strength-training"""
        try:
            response = requests.get(f"{self.base_url}/articles?category=strength-training", timeout=10)
            if response.status_code == 200:
                articles = response.json()
                if isinstance(articles, list):
                    # Check if filtered correctly
                    if articles:
                        # Verify all articles are in Strength Training category
                        strength_articles = [a for a in articles if a.get('category') == 'Strength Training']
                        if len(strength_articles) == len(articles):
                            print(f"   Found {len(articles)} strength training articles")
                            self.log_result("Get Articles by Category", True)
                            return True
                        else:
                            self.log_result("Get Articles by Category", False, "Category filter not working correctly")
                    else:
                        print("   No strength training articles found")
                        self.log_result("Get Articles by Category", True)  # Empty result is valid
                        return True
                else:
                    self.log_result("Get Articles by Category", False, "Response is not a list")
            else:
                self.log_result("Get Articles by Category", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get Articles by Category", False, f"Error: {str(e)}")
        return False
    
    def test_get_featured_articles(self):
        """Test GET /api/articles/featured"""
        try:
            response = requests.get(f"{self.base_url}/articles/featured", timeout=10)
            if response.status_code == 200:
                articles = response.json()
                if isinstance(articles, list):
                    # Verify all articles are featured
                    if articles:
                        featured_count = sum(1 for a in articles if a.get('featured') == True)
                        if featured_count == len(articles):
                            print(f"   Found {len(articles)} featured articles")
                            self.log_result("Get Featured Articles", True)
                            return articles
                        else:
                            self.log_result("Get Featured Articles", False, "Non-featured articles in featured endpoint")
                    else:
                        print("   No featured articles found")
                        self.log_result("Get Featured Articles", True)  # Empty result is valid
                        return []
                else:
                    self.log_result("Get Featured Articles", False, "Response is not a list")
            else:
                self.log_result("Get Featured Articles", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get Featured Articles", False, f"Error: {str(e)}")
        return []
    
    def test_get_article_by_id(self, articles):
        """Test GET /api/articles/{id}"""
        if not articles:
            self.log_result("Get Article by ID", False, "No articles available for testing")
            return False
            
        try:
            # Test with first article ID
            article_id = articles[0]['id']
            response = requests.get(f"{self.base_url}/articles/{article_id}", timeout=10)
            if response.status_code == 200:
                article = response.json()
                if article.get('id') == article_id:
                    print(f"   Retrieved article: {article.get('title', 'Unknown')}")
                    self.log_result("Get Article by ID", True)
                    return True
                else:
                    self.log_result("Get Article by ID", False, "Article ID mismatch")
            else:
                self.log_result("Get Article by ID", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get Article by ID", False, f"Error: {str(e)}")
        return False
    
    def test_get_invalid_article_id(self):
        """Test GET /api/articles/{invalid_id} - Should return 404"""
        try:
            invalid_id = "invalid-article-id-12345"
            response = requests.get(f"{self.base_url}/articles/{invalid_id}", timeout=10)
            if response.status_code == 404:
                self.log_result("Get Invalid Article ID (404)", True)
                return True
            else:
                self.log_result("Get Invalid Article ID (404)", False, f"Expected 404, got {response.status_code}")
        except Exception as e:
            self.log_result("Get Invalid Article ID (404)", False, f"Error: {str(e)}")
        return False
    
    def test_get_categories(self):
        """Test GET /api/categories"""
        try:
            response = requests.get(f"{self.base_url}/categories", timeout=10)
            if response.status_code == 200:
                categories = response.json()
                if isinstance(categories, list):
                    if categories:
                        # Should have "All Articles" category
                        all_category = next((c for c in categories if c.get('name') == 'All Articles'), None)
                        if all_category:
                            print(f"   Found {len(categories)} categories")
                            print(f"   Total articles count: {all_category.get('count', 0)}")
                            # Verify category structure
                            if all(key in categories[0] for key in ['id', 'name', 'count']):
                                self.log_result("Get Categories", True)
                                return categories
                            else:
                                self.log_result("Get Categories", False, "Invalid category structure")
                        else:
                            self.log_result("Get Categories", False, "Missing 'All Articles' category")
                    else:
                        self.log_result("Get Categories", False, "No categories found")
                else:
                    self.log_result("Get Categories", False, "Response is not a list")
            else:
                self.log_result("Get Categories", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get Categories", False, f"Error: {str(e)}")
        return []
    
    def test_newsletter_subscribe_valid(self):
        """Test POST /api/newsletter/subscribe with valid email"""
        try:
            test_email = "john.doe@fitlife.com"
            payload = {"email": test_email}
            response = requests.post(f"{self.base_url}/newsletter/subscribe", 
                                   json=payload, timeout=10)
            if response.status_code == 200:
                subscriber = response.json()
                if subscriber.get('email') == test_email and 'id' in subscriber:
                    print(f"   Subscribed: {test_email}")
                    self.log_result("Newsletter Subscribe (Valid)", True)
                    return subscriber
                else:
                    self.log_result("Newsletter Subscribe (Valid)", False, "Invalid subscriber response")
            else:
                self.log_result("Newsletter Subscribe (Valid)", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Newsletter Subscribe (Valid)", False, f"Error: {str(e)}")
        return None
    
    def test_newsletter_subscribe_duplicate(self):
        """Test POST /api/newsletter/subscribe with duplicate email"""
        try:
            test_email = "john.doe@fitlife.com"  # Same email as previous test
            payload = {"email": test_email}
            response = requests.post(f"{self.base_url}/newsletter/subscribe", 
                                   json=payload, timeout=10)
            if response.status_code == 200:
                subscriber = response.json()
                if subscriber.get('email') == test_email:
                    print(f"   Duplicate email handled gracefully: {test_email}")
                    self.log_result("Newsletter Subscribe (Duplicate)", True)
                    return True
                else:
                    self.log_result("Newsletter Subscribe (Duplicate)", False, "Invalid response for duplicate")
            else:
                self.log_result("Newsletter Subscribe (Duplicate)", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Newsletter Subscribe (Duplicate)", False, f"Error: {str(e)}")
        return False
    
    def test_newsletter_subscribe_invalid_email(self):
        """Test POST /api/newsletter/subscribe with invalid email"""
        try:
            invalid_email = "invalid-email-format"
            payload = {"email": invalid_email}
            response = requests.post(f"{self.base_url}/newsletter/subscribe", 
                                   json=payload, timeout=10)
            # Should return 422 for validation error
            if response.status_code == 422:
                self.log_result("Newsletter Subscribe (Invalid Email)", True)
                return True
            else:
                self.log_result("Newsletter Subscribe (Invalid Email)", False, 
                              f"Expected 422 validation error, got {response.status_code}")
        except Exception as e:
            self.log_result("Newsletter Subscribe (Invalid Email)", False, f"Error: {str(e)}")
        return False
    
    def test_get_newsletter_subscribers(self):
        """Test GET /api/newsletter/subscribers"""
        try:
            response = requests.get(f"{self.base_url}/newsletter/subscribers", timeout=10)
            if response.status_code == 200:
                subscribers = response.json()
                if isinstance(subscribers, list):
                    print(f"   Found {len(subscribers)} newsletter subscribers")
                    if subscribers:
                        # Verify subscriber structure
                        if all(key in subscribers[0] for key in ['id', 'email', 'subscribedAt']):
                            self.log_result("Get Newsletter Subscribers", True)
                            return subscribers
                        else:
                            self.log_result("Get Newsletter Subscribers", False, "Invalid subscriber structure")
                    else:
                        self.log_result("Get Newsletter Subscribers", True)  # Empty list is valid
                        return []
                else:
                    self.log_result("Get Newsletter Subscribers", False, "Response is not a list")
            else:
                self.log_result("Get Newsletter Subscribers", False, f"Status code: {response.status_code}")
        except Exception as e:
            self.log_result("Get Newsletter Subscribers", False, f"Error: {str(e)}")
        return []
    
    def run_all_tests(self):
        """Run all backend API tests"""
        print("🚀 Starting FitLife Blog Backend API Tests")
        print(f"📡 Testing API at: {self.base_url}")
        print("=" * 60)
        
        # Test API health first
        if not self.test_health_check():
            print("❌ API is not responding. Stopping tests.")
            return self.test_results
        
        print("\n📚 Testing Articles Endpoints:")
        articles = self.test_get_all_articles()
        self.test_get_articles_by_category()
        featured_articles = self.test_get_featured_articles()
        self.test_get_article_by_id(articles)
        self.test_get_invalid_article_id()
        
        print("\n🏷️ Testing Categories Endpoint:")
        categories = self.test_get_categories()
        
        print("\n📧 Testing Newsletter Endpoints:")
        self.test_newsletter_subscribe_valid()
        self.test_newsletter_subscribe_duplicate()
        self.test_newsletter_subscribe_invalid_email()
        self.test_get_newsletter_subscribers()
        
        print("\n" + "=" * 60)
        print(f"📊 Test Results: {self.test_results['passed']} passed, {self.test_results['failed']} failed")
        
        if self.test_results['errors']:
            print("\n❌ Failed Tests:")
            for error in self.test_results['errors']:
                print(f"   • {error}")
        
        return self.test_results

def main():
    """Main test runner"""
    tester = FitLifeAPITester()
    results = tester.run_all_tests()
    
    # Exit with error code if tests failed
    if results['failed'] > 0:
        sys.exit(1)
    else:
        print("\n🎉 All tests passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()