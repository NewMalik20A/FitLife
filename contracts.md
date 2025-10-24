# FitLife Blog - Backend Integration Contracts

## Mock Data to Remove
- `/app/frontend/src/mock.js` - All mock data and functions will be replaced with API calls

## Database Collections

### 1. Articles Collection
```javascript
{
  _id: ObjectId,
  title: String,
  excerpt: String,
  content: String,
  category: String,
  author: String,
  publishDate: Date,
  readTime: String,
  image: String,
  featured: Boolean,
  createdAt: Date,
  updatedAt: Date
}
```

### 2. Categories Collection
```javascript
{
  _id: ObjectId,
  id: String (slug),
  name: String,
  count: Number (computed from articles)
}
```

### 3. Newsletter Subscribers Collection
```javascript
{
  _id: ObjectId,
  email: String (unique),
  subscribedAt: Date
}
```

## API Endpoints

### Articles
- `GET /api/articles` - Get all articles (with optional ?category=slug query)
- `GET /api/articles/:id` - Get single article by ID
- `GET /api/articles/featured` - Get featured articles only
- `POST /api/articles` - Create new article (for future admin)
- `PUT /api/articles/:id` - Update article (for future admin)
- `DELETE /api/articles/:id` - Delete article (for future admin)

### Categories
- `GET /api/categories` - Get all categories with article counts

### Newsletter
- `POST /api/newsletter/subscribe` - Subscribe email to newsletter
- `GET /api/newsletter/subscribers` - Get all subscribers (for future admin)

## Frontend Integration Changes

### Files to Update:
1. **HomePage.jsx** - Replace `getFeaturedPosts()` with API call to `/api/articles/featured`
2. **BlogPage.jsx** - Replace `getPostsByCategory()` with API call to `/api/articles?category=`
3. **ArticlePage.jsx** - Replace `getPostById()` with API call to `/api/articles/:id`
4. **NewsletterSection.jsx** - Replace `subscribeToNewsletter()` with API POST to `/api/newsletter/subscribe`

### API Service Creation:
Create `/app/frontend/src/services/api.js` for centralized API calls using axios

## Implementation Steps

1. Create MongoDB models in `/app/backend/models/`
2. Create API routes in `/app/backend/routes/`
3. Update `server.py` to include new routes
4. Seed database with initial articles from mock data
5. Create API service in frontend
6. Update all components to use API instead of mock
7. Test all endpoints and frontend integration
