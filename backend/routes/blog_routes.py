from fastapi import APIRouter, HTTPException, Query, Depends
from typing import List, Optional
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

from models.blog_models import (
    Article, ArticleCreate, ArticleUpdate,
    Category, NewsletterSubscriber, NewsletterSubscribe
)

ROOT_DIR = Path(__file__).parent.parent
load_dotenv(ROOT_DIR / '.env')

router = APIRouter()

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Articles Routes
@router.get("/articles", response_model=List[Article])
async def get_articles(category: Optional[str] = Query(None)):
    """Get all articles with optional category filter"""
    try:
        query = {}
        if category and category != 'all':
            # Convert slug to category name
            category_name = category.replace('-', ' ').title()
            query = {"category": category_name}
        
        articles = await db.articles.find(query).sort("publishDate", -1).to_list(1000)
        return [Article(**article) for article in articles]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/articles/featured", response_model=List[Article])
async def get_featured_articles():
    """Get featured articles only"""
    try:
        articles = await db.articles.find({"featured": True}).sort("publishDate", -1).to_list(100)
        return [Article(**article) for article in articles]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/articles/{article_id}", response_model=Article)
async def get_article(article_id: str):
    """Get single article by ID"""
    try:
        article = await db.articles.find_one({"id": article_id})
        if not article:
            raise HTTPException(status_code=404, detail="Article not found")
        return Article(**article)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/articles", response_model=Article)
async def create_article(article: ArticleCreate):
    """Create new article"""
    try:
        article_dict = article.model_dump()
        new_article = Article(**article_dict)
        await db.articles.insert_one(new_article.model_dump())
        return new_article
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/articles/{article_id}", response_model=Article)
async def update_article(article_id: str, article: ArticleUpdate):
    """Update existing article"""
    try:
        update_data = {k: v for k, v in article.model_dump().items() if v is not None}
        update_data["updatedAt"] = datetime.utcnow()
        
        result = await db.articles.update_one(
            {"id": article_id},
            {"$set": update_data}
        )
        
        if result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Article not found")
        
        updated_article = await db.articles.find_one({"id": article_id})
        return Article(**updated_article)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/articles/{article_id}")
async def delete_article(article_id: str):
    """Delete article"""
    try:
        result = await db.articles.delete_one({"id": article_id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Article not found")
        return {"message": "Article deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Categories Routes
@router.get("/categories", response_model=List[Category])
async def get_categories():
    """Get all categories with article counts"""
    try:
        # Get total count
        total_count = await db.articles.count_documents({})
        
        # Get counts by category
        pipeline = [
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"_id": 1}}
        ]
        category_counts = await db.articles.aggregate(pipeline).to_list(100)
        
        # Build categories list
        categories = [
            Category(id="all", name="All Articles", count=total_count)
        ]
        
        for cat in category_counts:
            slug = cat["_id"].lower().replace(" ", "-")
            categories.append(
                Category(id=slug, name=cat["_id"], count=cat["count"])
            )
        
        return categories
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Newsletter Routes
@router.post("/newsletter/subscribe", response_model=NewsletterSubscriber)
async def subscribe_newsletter(subscriber: NewsletterSubscribe):
    """Subscribe to newsletter"""
    try:
        # Check if email already exists
        existing = await db.newsletter_subscribers.find_one({"email": subscriber.email})
        if existing:
            return NewsletterSubscriber(**existing)
        
        # Create new subscriber
        new_subscriber = NewsletterSubscriber(email=subscriber.email)
        await db.newsletter_subscribers.insert_one(new_subscriber.model_dump())
        return new_subscriber
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/newsletter/subscribers", response_model=List[NewsletterSubscriber])
async def get_subscribers():
    """Get all newsletter subscribers"""
    try:
        subscribers = await db.newsletter_subscribers.find().sort("subscribedAt", -1).to_list(10000)
        return [NewsletterSubscriber(**sub) for sub in subscribers]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))