import React, { useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { ArrowLeft, Clock, User, Calendar } from 'lucide-react';
import Header from '../components/Header';
import Footer from '../components/Footer';
import { getPostById, blogPosts } from '../mock';
import './ArticlePage.css';

const ArticlePage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const article = getPostById(id);

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [id]);

  if (!article) {
    return (
      <div className="article-page">
        <Header />
        <div className="container" style={{ paddingTop: '150px', textAlign: 'center' }}>
          <h1 className="heading-1">Article not found</h1>
          <Link to="/blog" className="btn-primary" style={{ marginTop: '24px' }}>
            Back to Articles
          </Link>
        </div>
        <Footer />
      </div>
    );
  }

  const relatedPosts = blogPosts
    .filter(post => post.id !== article.id && post.category === article.category)
    .slice(0, 3);

  return (
    <div className="article-page">
      <Header />
      
      <article className="article-container">
        <div className="article-hero">
          <div className="container">
            <button onClick={() => navigate('/blog')} className="back-button">
              <ArrowLeft size={20} /> Back to Articles
            </button>
            
            <span className="article-hero-category">{article.category}</span>
            <h1 className="display-medium article-title">{article.title}</h1>
            
            <div className="article-hero-meta">
              <div className="meta-item">
                <User size={18} />
                <span>{article.author}</span>
              </div>
              <div className="meta-item">
                <Calendar size={18} />
                <span>{new Date(article.publishDate).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })}</span>
              </div>
              <div className="meta-item">
                <Clock size={18} />
                <span>{article.readTime}</span>
              </div>
            </div>
          </div>
        </div>

        <div className="article-featured-image">
          <img src={article.image} alt={article.title} />
        </div>

        <div className="container">
          <div className="article-content-wrapper">
            <div className="article-body">
              <p className="article-excerpt">{article.excerpt}</p>
              
              <h2 className="heading-2">Introduction</h2>
              <p className="body-large">
                {article.content} This comprehensive guide will walk you through everything you need to know to achieve your fitness goals effectively and sustainably.
              </p>

              <h2 className="heading-2">Key Principles</h2>
              <p className="body-large">
                Understanding the fundamentals is crucial for long-term success. Whether you're just starting out or looking to refine your approach, these core concepts will help you make informed decisions about your training and nutrition.
              </p>

              <h3 className="heading-3">Progressive Overload</h3>
              <p className="body-large">
                Progressive overload is the foundation of any successful training program. By gradually increasing the demands on your body, you stimulate continuous adaptation and improvement. This can be achieved through various methods including increasing weight, volume, or training frequency.
              </p>

              <h3 className="heading-3">Recovery and Adaptation</h3>
              <p className="body-large">
                Your body doesn't grow in the gym—it grows during recovery. Adequate rest, quality sleep, and proper nutrition are essential for allowing your body to repair and adapt to the training stimulus. Never underestimate the importance of rest days in your program.
              </p>

              <h2 className="heading-2">Practical Application</h2>
              <p className="body-large">
                Now that we've covered the theory, let's discuss how to apply these principles in your training. Start with a solid foundation and build gradually over time. Consistency is more important than perfection, so focus on developing sustainable habits that you can maintain long-term.
              </p>

              <h2 className="heading-2">Conclusion</h2>
              <p className="body-large">
                Success in fitness is a journey, not a destination. By applying the principles discussed in this article and staying consistent with your efforts, you'll be well on your way to achieving your goals. Remember to track your progress, adjust as needed, and most importantly—enjoy the process!
              </p>
            </div>
          </div>
        </div>
      </article>

      {relatedPosts.length > 0 && (
        <section className="related-section">
          <div className="container">
            <h2 className="heading-2">Related Articles</h2>
            <div className="related-grid">
              {relatedPosts.map(post => (
                <Link to={`/article/${post.id}`} key={post.id} className="related-card">
                  <div className="related-image">
                    <img src={post.image} alt={post.title} />
                  </div>
                  <div className="related-content">
                    <span className="related-category">{post.category}</span>
                    <h3 className="heading-3">{post.title}</h3>
                    <p className="body-small">{post.readTime}</p>
                  </div>
                </Link>
              ))}
            </div>
          </div>
        </section>
      )}

      <Footer />
    </div>
  );
};

export default ArticlePage;