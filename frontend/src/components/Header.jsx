import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Menu, X } from 'lucide-react';
import './Header.css';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="network-header">
      <div className="nav-wrapper">
        <Link to="/" className="network-logo">
          FitLife
        </Link>
        
        <button 
          className="mobile-menu-btn"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          aria-label="Toggle menu"
        >
          {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
        </button>

        <nav className={`network-nav ${isMenuOpen ? 'open' : ''}`}>
          <Link to="/" className="network-nav-link" onClick={() => setIsMenuOpen(false)}>
            Home
          </Link>
          <Link to="/blog" className="network-nav-link" onClick={() => setIsMenuOpen(false)}>
            Articles
          </Link>
          <Link to="/blog" className="network-nav-link" onClick={() => setIsMenuOpen(false)}>
            Categories
          </Link>
          <a href="#newsletter" className="btn-primary nav-cta" onClick={() => setIsMenuOpen(false)}>
            Subscribe
          </a>
        </nav>
      </div>
    </header>
  );
};

export default Header;