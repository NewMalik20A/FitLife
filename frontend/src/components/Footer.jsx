import React from 'react';
import { Heart, Github, Twitter, Instagram } from 'lucide-react';
import './Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-content">
          <div className="footer-brand">
            <h3 className="footer-logo">FitLife</h3>
            <p className="body-small">
              Your trusted source for fitness knowledge, training tips, and wellness insights.
            </p>
            <div className="social-links">
              <a href="#" aria-label="Twitter" className="social-link">
                <Twitter size={20} />
              </a>
              <a href="#" aria-label="Instagram" className="social-link">
                <Instagram size={20} />
              </a>
              <a href="#" aria-label="Github" className="social-link">
                <Github size={20} />
              </a>
            </div>
          </div>

          <div className="footer-links">
            <div className="footer-column">
              <h4 className="footer-heading">Content</h4>
              <ul>
                <li><a href="#">All Articles</a></li>
                <li><a href="#">Strength Training</a></li>
                <li><a href="#">Cardio</a></li>
                <li><a href="#">Nutrition</a></li>
              </ul>
            </div>

            <div className="footer-column">
              <h4 className="footer-heading">Resources</h4>
              <ul>
                <li><a href="#">Training Guides</a></li>
                <li><a href="#">Meal Plans</a></li>
                <li><a href="#">Workout Programs</a></li>
                <li><a href="#">FAQ</a></li>
              </ul>
            </div>

            <div className="footer-column">
              <h4 className="footer-heading">Company</h4>
              <ul>
                <li><a href="#">About Us</a></li>
                <li><a href="#">Our Team</a></li>
                <li><a href="#">Contact</a></li>
                <li><a href="#">Careers</a></li>
              </ul>
            </div>
          </div>
        </div>

        <div className="footer-bottom">
          <p className="body-small">
            © 2025 FitLife Blog. Made with <Heart size={16} className="heart-icon" /> for fitness enthusiasts.
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;