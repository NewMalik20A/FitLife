import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, TrendingUp, Users, BookOpen } from 'lucide-react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import NewsletterSection from '../components/NewsletterSection';
import { articlesApi } from '../services/api';
import './HomePage.css';

const HomePage = () => {
  const [featuredPosts, setFeaturedPosts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchFeaturedPosts = async () => {
      try {
        const posts = await articlesApi.getFeatured();
        setFeaturedPosts(posts);
      } catch (error) {
        console.error('Error fetching featured posts:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchFeaturedPosts();
  }, []);

  return (
    <div className="home-page">
      <Header />
      
      {/* Hero Section */}
      <section className="hero-section">
        <div className="container">
          <div className="hero-content">
            <h1 className="display-large">
              Transform Your Fitness Journey
            </h1>
            <p className="body-large hero-subtitle">
              Expert insights, proven strategies, and science-backed advice to help you reach your fitness goals.
            </p>
            <div className="hero-cta">
              <Link to="/blog" className="btn-primary btn-large">
                Explore Articles <ArrowRight size={20} />
              </Link>
              <a href="#newsletter" className="btn-secondary btn-large">
                Subscribe Now
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Stats Section */}
      <section className="stats-section">
        <div className="container">
          <div className="stats-grid">
            <div className="stat-card">
              <div className="stat-icon">
                <BookOpen size={32} />
              </div>
              <div className="stat-number">500+</div>
              <div className="stat-label">Articles Published</div>
            </div>
            <div className="stat-card">
              <div className="stat-icon">
                <Users size={32} />
              </div>
              <div className="stat-number">50K+</div>
              <div className="stat-label">Active Readers</div>
            </div>
            <div className="stat-card">
              <div className="stat-icon">
                <TrendingUp size={32} />
              </div>
              <div className="stat-number">95%</div>
              <div className="stat-label">Success Rate</div>
            </div>
          </div>
        </div>
      </section>

      {/* Featured Articles */}
      <section className="featured-section">
        <div className="container">
          <div className="section-header">
            <h2 className="heading-1">Featured Articles</h2>
            <p className="body-large">Handpicked stories to kickstart your fitness transformation</p>
          </div>
          {loading ? (
            <div className="loading-message">Loading articles...</div>
          ) : (
            <>
              <div className="featured-grid">
                {featuredPosts.map((post) => (
                  <Link to={`/article/${post.id}`} key={post.id} className="featured-card">
                    <div className="featured-image">
                      <img src={post.image} alt={post.title} />
                      <span className="category-badge">{post.category}</span>
                    </div>
                    <div className="featured-content">
                      <h3 className="heading-3">{post.title}</h3>
                      <p className="body-medium">{post.excerpt}</p>
                      <div className="featured-meta">
                        <span className="author">{post.author}</span>
                        <span className="read-time">{post.readTime}</span>
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
              <div className="section-cta">
                <Link to="/blog" className="btn-secondary">
                  View All Articles <ArrowRight size={18} />
                </Link>
              </div>
            </>
          )}
        </div>
      </section>

      {/* Why Choose Us */}
      <section className="why-section">
        <div className="container">
          <h2 className="heading-1 text-center">Why FitLife Blog?</h2>
          <div className="why-grid">
            <div className="network-card">
              <h3 className="heading-3">Expert Contributors</h3>
              <p className="body-medium">
                Learn from certified trainers, nutritionists, and fitness professionals with years of real-world experience.
              </p>
            </div>
            <div className="network-card">
              <h3 className="heading-3">Science-Backed Content</h3>
              <p className="body-medium">
                Every article is researched and verified to ensure you get accurate, reliable fitness information.
              </p>
            </div>
            <div className="network-card">
              <h3 className="heading-3">Practical Guides</h3>
              <p className="body-medium">
                Actionable advice you can implement immediately, from beginner basics to advanced techniques.
              </p>
            </div>
          </div>
        </div>
      </section>

      <NewsletterSection />
      <Footer />
    </div>
  );
};

export default HomePage;