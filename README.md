# FitLife Blog - Fitness Content Platform

A modern, full-stack fitness blog platform built with React, FastAPI, and MongoDB. Features article management, category filtering, search functionality, and newsletter subscriptions.

![FitLife Blog](https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=1200&h=400&fit=crop)

## 🚀 Features

- **Article Management**: Browse, search, and read fitness articles
- **Category Filtering**: Filter articles by Strength Training, Cardio, Nutrition, etc.
- **Search Functionality**: Real-time search across articles
- **Featured Articles**: Highlight important content on the homepage
- **Newsletter Subscription**: Email subscription with duplicate handling
- **Responsive Design**: Mobile-first design that works on all devices
- **Modern UI**: Clean, professional design with smooth animations

## 🛠️ Tech Stack

### Frontend
- **React 19** - UI framework
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Lucide React** - Icon library
- **Tailwind CSS** - Utility-first CSS framework

### Backend
- **FastAPI** - Modern Python web framework
- **MongoDB** - NoSQL database
- **Motor** - Async MongoDB driver
- **Pydantic** - Data validation

## 📋 Prerequisites

- **Docker** (version 20.10 or higher)
- **Docker Compose** (version 2.0 or higher)

## 🚀 Quick Start with Docker

### 1. Clone or Extract the Project

```bash
cd fitlife-blog
```

### 2. Configure Environment Variables

The project includes a `.env.production` file with default settings. For production deployment, update the backend URL:

```bash
# Edit .env.production
REACT_APP_BACKEND_URL=http://your-domain.com:8001
```

### 3. Build and Run with Docker Compose

```bash
# Build and start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Stop and remove volumes (WARNING: This deletes all data)
docker-compose down -v
```

### 4. Seed the Database

After the services are running, seed the database with sample articles:

```bash
docker-compose exec backend python seed_data.py
```

### 5. Access the Application

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8001
- **API Documentation**: http://localhost:8001/docs
- **MongoDB**: localhost:27017

## 📁 Project Structure

```
fitlife-blog/
├── frontend/                 # React frontend application
│   ├── public/              # Static files
│   ├── src/
│   │   ├── components/      # Reusable components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API service layer
│   │   └── App.js           # Main app component
│   ├── package.json
│   └── tailwind.config.js
│
├── backend/                  # FastAPI backend application
│   ├── models/              # Pydantic models
│   ├── routes/              # API routes
│   ├── server.py            # Main application file
│   ├── seed_data.py         # Database seeding script
│   └── requirements.txt     # Python dependencies
│
├── docker-compose.yml        # Docker Compose configuration
├── Dockerfile.backend        # Backend Docker image
├── Dockerfile.frontend       # Frontend Docker image
├── nginx.conf               # Nginx configuration for frontend
└── README.md                # This file
```

## 🔧 Development Setup

### Running Without Docker

#### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
MONGO_URL=mongodb://localhost:27017
DB_NAME=fitlife_db
EOF

# Start MongoDB (if not using Docker)
# Install and run MongoDB locally or use a cloud instance

# Run the backend
uvicorn server:app --host 0.0.0.0 --port 8001 --reload

# Seed the database (in another terminal)
python seed_data.py
```

#### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
yarn install

# Create .env file
cat > .env << EOF
REACT_APP_BACKEND_URL=http://localhost:8001
EOF

# Start the development server
yarn start
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend: http://localhost:8001

## 📡 API Endpoints

### Articles
- `GET /api/articles` - Get all articles (optional ?category=slug)
- `GET /api/articles/featured` - Get featured articles
- `GET /api/articles/{id}` - Get article by ID
- `POST /api/articles` - Create new article
- `PUT /api/articles/{id}` - Update article
- `DELETE /api/articles/{id}` - Delete article

### Categories
- `GET /api/categories` - Get all categories with article counts

### Newsletter
- `POST /api/newsletter/subscribe` - Subscribe to newsletter
- `GET /api/newsletter/subscribers` - Get all subscribers

### Full API Documentation
Visit http://localhost:8001/docs for interactive Swagger documentation.

## 🗄️ Database Schema

### Articles Collection
```javascript
{
  id: String (UUID),
  title: String,
  excerpt: String,
  content: String,
  category: String,
  author: String,
  publishDate: DateTime,
  readTime: String,
  image: String (URL),
  featured: Boolean,
  createdAt: DateTime,
  updatedAt: DateTime
}
```

### Newsletter Subscribers Collection
```javascript
{
  id: String (UUID),
  email: String (unique),
  subscribedAt: DateTime
}
```

## 🎨 Customization

### Changing Colors

Edit `/app/frontend/src/App.css` to customize the color scheme:

```css
:root {
  --bg-page: #FAFFEE;
  --brand-primary: #D3FF62;
  --brand-dark: #004534;
  --text-primary: #004534;
  /* ... more variables */
}
```

### Adding New Articles

Use the API endpoints or seed script to add articles:

```python
# Add to backend/seed_data.py
{
    'id': '9',
    'title': 'Your Article Title',
    'excerpt': 'Article summary...',
    'content': 'Full article content...',
    'category': 'Your Category',
    'author': 'Author Name',
    'publishDate': datetime(2025, 8, 20),
    'readTime': '5 min read',
    'image': 'https://your-image-url.com',
    'featured': True
}
```

## 🐛 Troubleshooting

### Port Already in Use

If ports 3000, 8001, or 27017 are already in use:

```bash
# Edit docker-compose.yml and change port mappings
# For example, change "3000:80" to "3001:80"
```

### Database Connection Issues

```bash
# Check if MongoDB is running
docker-compose ps

# View MongoDB logs
docker-compose logs mongodb

# Restart MongoDB service
docker-compose restart mongodb
```

### Frontend Not Loading

```bash
# Rebuild frontend with no cache
docker-compose build --no-cache frontend
docker-compose up -d frontend
```

### Clear All Data and Restart

```bash
# Stop everything and remove volumes
docker-compose down -v

# Rebuild and start
docker-compose up -d --build

# Reseed database
docker-compose exec backend python seed_data.py
```

## 📦 Production Deployment

### Environment Variables for Production

Update `.env.production` with your production values:

```env
MONGO_URL=mongodb://your-mongodb-host:27017
DB_NAME=fitlife_db
REACT_APP_BACKEND_URL=https://api.yourdomain.com
```

### Build Production Images

```bash
# Build with production environment
docker-compose -f docker-compose.yml build

# Deploy to your server
# Copy docker-compose.yml and .env.production to your server
# Run: docker-compose up -d
```

### Nginx Reverse Proxy (Optional)

For serving both frontend and backend from the same domain:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8001;
    }
}
```

## 🔒 Security Considerations

1. **Change Default MongoDB Credentials**: Add authentication to MongoDB in production
2. **Use HTTPS**: Configure SSL certificates for production
3. **Environment Variables**: Never commit `.env` files with sensitive data
4. **CORS Configuration**: Restrict allowed origins in production
5. **Rate Limiting**: Implement rate limiting on API endpoints
6. **Input Validation**: All inputs are validated on backend with Pydantic

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on the project repository.

---

**Built with ❤️ for fitness enthusiasts**
