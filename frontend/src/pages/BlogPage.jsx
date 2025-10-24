import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Search } from 'lucide-react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { articlesApi, categoriesApi } from '../services/api';
import './BlogPage.css';

const BlogPage = () => {
  const [activeCategory, setActiveCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [articles, setArticles] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [articlesData, categoriesData] = await Promise.all([
          articlesApi.getAll(),
          categoriesApi.getAll()
        ]);
        setArticles(articlesData);
        setCategories(categoriesData);
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  useEffect(() => {
    const fetchArticlesByCategory = async () => {
      try {
        setLoading(true);
        const articlesData = await articlesApi.getAll(activeCategory === 'all' ? null : activeCategory);
        setArticles(articlesData);
      } catch (error) {
        console.error('Error fetching articles:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchArticlesByCategory();
  }, [activeCategory]);

  const filteredPosts = articles.filter(post =>
    post.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
    post.excerpt.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="blog-page">
      <Header />
      
      <div className="blog-header-section">
        <div className="container">
          <h1 className="display-medium">Fitness Articles & Guides</h1>
          <p className="body-large">Explore our library of expert fitness content</p>
          
          <div className="search-bar">
            <Search size={20} className="search-icon" />
            <input
              type="text"
              placeholder="Search articles..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="search-input"
            />
          </div>
        </div>
      </div>

      <div className="container">
        <div className="blog-layout">
          <aside className="blog-sidebar">
            <div className="sidebar-section">
              <h3 className="heading-3">Categories</h3>
              <ul className="category-list">
                {categories.map(cat => (
                  <li key={cat.id}>
                    <button
                      onClick={() => setActiveCategory(cat.id)}
                      className={`category-btn ${activeCategory === cat.id ? 'active' : ''}`}
                    >
                      {cat.name} <span className="count">({cat.count})</span>
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          </aside>

          <main className="blog-main">
            {loading ? (
              <div className="loading-message">Loading articles...</div>
            ) : filteredPosts.length === 0 ? (
              <div className="no-results">
                <p className="body-large">No articles found matching your search.</p>
              </div>
            ) : (
              <div className="articles-grid">
                {filteredPosts.map(post => (
                  <Link to={`/article/${post.id}`} key={post.id} className="article-card">
                    <div className="article-image">
                      <img src={post.image} alt={post.title} />
                      <span className="article-category">{post.category}</span>
                    </div>
                    <div className="article-content">
                      <h3 className="heading-3">{post.title}</h3>
                      <p className="body-medium">{post.excerpt}</p>
                      <div className="article-meta">
                        <span className="author">{post.author}</span>
                        <span className="separator">•</span>
                        <span className="read-time">{post.readTime}</span>
                      </div>
                    </div>
                  </Link>
                ))}
              </div>
            )}
          </main>
        </div>
      </div>

      <Footer />
    </div>
  );
};

export default BlogPage;