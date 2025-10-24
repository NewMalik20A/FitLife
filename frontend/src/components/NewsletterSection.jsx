import React, { useState } from 'react';
import { Mail } from 'lucide-react';
import { newsletterApi } from '../services/api';
import './NewsletterSection.css';

const NewsletterSection = () => {
  const [email, setEmail] = useState('');
  const [subscribed, setSubscribed] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (email) {
      try {
        setLoading(true);
        setError('');
        await newsletterApi.subscribe(email);
        setSubscribed(true);
        setEmail('');
        setTimeout(() => setSubscribed(false), 3000);
      } catch (error) {
        console.error('Error subscribing:', error);
        setError('Failed to subscribe. Please try again.');
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <section className="newsletter-section" id="newsletter">
      <div className="container">
        <div className="newsletter-card">
          <div className="newsletter-icon">
            <Mail size={48} />
          </div>
          <h2 className="heading-2">Stay in the Loop</h2>
          <p className="body-large">
            Get the latest fitness tips, training guides, and nutrition advice delivered to your inbox every week.
          </p>
          {subscribed ? (
            <div className="success-message">
              <p>🎉 Thanks for subscribing! Check your inbox for confirmation.</p>
            </div>
          ) : (
            <>
              <form onSubmit={handleSubmit} className="newsletter-form">
                <input
                  type="email"
                  placeholder="Enter your email address"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  disabled={loading}
                  className="newsletter-input"
                />
                <button type="submit" className="btn-primary" disabled={loading}>
                  {loading ? 'Subscribing...' : 'Subscribe'}
                </button>
              </form>
              {error && <p className="error-message">{error}</p>}
            </>
          )}
          <p className="body-small newsletter-privacy">
            We respect your privacy. Unsubscribe at any time.
          </p>
        </div>
      </div>
    </section>
  );
};

export default NewsletterSection;