# FitLife Blog - Docker Deployment Guide

This guide provides detailed instructions for deploying FitLife Blog using Docker.

## Table of Contents
- [Quick Start](#quick-start)
- [Manual Docker Commands](#manual-docker-commands)
- [Environment Configuration](#environment-configuration)
- [Production Deployment](#production-deployment)
- [Troubleshooting](#troubleshooting)

## Quick Start

### For Linux/Mac:
```bash
./start.sh
```

### For Windows:
```cmd
start.bat
```

That's it! The script will:
1. Build all Docker images
2. Start MongoDB, Backend, and Frontend services
3. Seed the database with sample articles
4. Display access URLs

## Manual Docker Commands

If you prefer to run commands manually:

### 1. Build Images
```bash
docker-compose build
```

### 2. Start Services
```bash
docker-compose up -d
```

### 3. Check Status
```bash
docker-compose ps
```

### 4. View Logs
```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f frontend
docker-compose logs -f mongodb
```

### 5. Seed Database
```bash
docker-compose exec backend python seed_data.py
```

### 6. Stop Services
```bash
docker-compose down
```

### 7. Stop and Remove Data
```bash
docker-compose down -v
```

## Environment Configuration

### Development Environment

The default configuration works for local development:

```yaml
# docker-compose.yml
environment:
  - MONGO_URL=mongodb://mongodb:27017
  - DB_NAME=fitlife_db
```

Frontend will connect to backend at `http://localhost:8001`

### Production Environment

For production deployment, update the following:

#### 1. Update Backend URL in docker-compose.yml

```yaml
frontend:
  build:
    args:
      - REACT_APP_BACKEND_URL=https://api.yourdomain.com
```

#### 2. Add MongoDB Authentication

```yaml
mongodb:
  environment:
    MONGO_INITDB_ROOT_USERNAME: admin
    MONGO_INITDB_ROOT_PASSWORD: your_secure_password
    MONGO_INITDB_DATABASE: fitlife_db

backend:
  environment:
    - MONGO_URL=mongodb://admin:your_secure_password@mongodb:27017
    - DB_NAME=fitlife_db
```

#### 3. Use Environment File

Create `.env` file:
```env
MONGO_USERNAME=admin
MONGO_PASSWORD=your_secure_password
MONGO_DATABASE=fitlife_db
BACKEND_URL=https://api.yourdomain.com
```

Update docker-compose.yml:
```yaml
mongodb:
  environment:
    MONGO_INITDB_ROOT_USERNAME: ${MONGO_USERNAME}
    MONGO_INITDB_ROOT_PASSWORD: ${MONGO_PASSWORD}
    MONGO_INITDB_DATABASE: ${MONGO_DATABASE}

backend:
  environment:
    - MONGO_URL=mongodb://${MONGO_USERNAME}:${MONGO_PASSWORD}@mongodb:27017
    - DB_NAME=${MONGO_DATABASE}

frontend:
  build:
    args:
      - REACT_APP_BACKEND_URL=${BACKEND_URL}
```

## Production Deployment

### Option 1: Deploy to VPS/Cloud Server

1. **Install Docker on your server**
```bash
# Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

2. **Copy project to server**
```bash
# From your local machine
scp -r fitlife-blog user@your-server-ip:/home/user/
```

3. **Configure for production**
```bash
# On your server
cd /home/user/fitlife-blog
nano .env  # Add production environment variables
```

4. **Run the application**
```bash
./start.sh
```

### Option 2: Deploy with Nginx Reverse Proxy

If you want to serve both frontend and backend from the same domain:

1. **Create nginx configuration** (`/etc/nginx/sites-available/fitlife`)
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # Frontend
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }

    # Backend API
    location /api {
        proxy_pass http://localhost:8001;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

2. **Enable site and restart nginx**
```bash
sudo ln -s /etc/nginx/sites-available/fitlife /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

3. **Update frontend build to use relative URLs**
```yaml
frontend:
  build:
    args:
      - REACT_APP_BACKEND_URL=  # Empty for same domain
```

### Option 3: Deploy with SSL/HTTPS

1. **Install Certbot**
```bash
sudo apt-get update
sudo apt-get install certbot python3-certbot-nginx
```

2. **Get SSL certificate**
```bash
sudo certbot --nginx -d yourdomain.com
```

3. **Update docker-compose.yml**
```yaml
frontend:
  build:
    args:
      - REACT_APP_BACKEND_URL=https://yourdomain.com
```

## Docker Image Management

### Build Specific Service
```bash
docker-compose build backend
docker-compose build frontend
```

### Rebuild Without Cache
```bash
docker-compose build --no-cache
```

### View Image Sizes
```bash
docker images | grep fitlife
```

### Clean Up Unused Images
```bash
docker image prune
docker system prune -a
```

## Data Management

### Backup MongoDB Data
```bash
# Create backup
docker-compose exec mongodb mongodump --out=/backup
docker cp fitlife-mongodb:/backup ./mongodb-backup

# Restore backup
docker cp ./mongodb-backup fitlife-mongodb:/backup
docker-compose exec mongodb mongorestore /backup
```

### Export Articles
```bash
docker-compose exec mongodb mongoexport \
  --db=fitlife_db \
  --collection=articles \
  --out=/tmp/articles.json

docker cp fitlife-mongodb:/tmp/articles.json ./
```

### Import Articles
```bash
docker cp ./articles.json fitlife-mongodb:/tmp/
docker-compose exec mongodb mongoimport \
  --db=fitlife_db \
  --collection=articles \
  --file=/tmp/articles.json
```

## Monitoring and Logs

### Real-time Logs
```bash
# All services
docker-compose logs -f --tail=100

# Specific service with timestamps
docker-compose logs -f --tail=100 -t backend
```

### Container Stats
```bash
docker stats fitlife-mongodb fitlife-backend fitlife-frontend
```

### Health Checks
```bash
# Check if services are healthy
docker-compose ps

# Check backend health
curl http://localhost:8001/api/

# Check frontend
curl http://localhost:3000
```

## Troubleshooting

### Services Won't Start

1. **Check Docker is running**
```bash
docker --version
docker-compose --version
```

2. **Check port conflicts**
```bash
# Check if ports are in use
lsof -i :3000
lsof -i :8001
lsof -i :27017

# Kill process using port
kill -9 <PID>
```

3. **Check logs for errors**
```bash
docker-compose logs --tail=50 backend
```

### MongoDB Connection Issues

1. **Verify MongoDB is running**
```bash
docker-compose ps mongodb
```

2. **Check MongoDB logs**
```bash
docker-compose logs mongodb
```

3. **Test MongoDB connection**
```bash
docker-compose exec mongodb mongosh
```

### Frontend Not Loading

1. **Check if backend is accessible**
```bash
curl http://localhost:8001/api/articles
```

2. **Verify environment variables**
```bash
docker-compose exec frontend env | grep REACT_APP
```

3. **Rebuild frontend**
```bash
docker-compose build --no-cache frontend
docker-compose up -d frontend
```

### Database Not Seeding

1. **Manually run seed script**
```bash
docker-compose exec backend python seed_data.py
```

2. **Check if MongoDB is ready**
```bash
docker-compose logs mongodb | grep "waiting for connections"
```

3. **Verify database connection**
```bash
docker-compose exec backend python -c "from motor.motor_asyncio import AsyncIOMotorClient; import os; print('Testing connection...'); client = AsyncIOMotorClient(os.environ['MONGO_URL']); print('Connected!')"
```

### Reset Everything

If all else fails, complete reset:

```bash
# Stop and remove everything
docker-compose down -v

# Remove all fitlife images
docker images | grep fitlife | awk '{print $3}' | xargs docker rmi -f

# Rebuild and start
docker-compose build --no-cache
docker-compose up -d

# Wait and seed
sleep 30
docker-compose exec backend python seed_data.py
```

## Performance Optimization

### Use Build Cache
```bash
# Default behavior uses cache
docker-compose build
```

### Multi-stage Build Optimization
The Dockerfiles are already optimized with multi-stage builds:
- Frontend: node:18-alpine → nginx:alpine (reduces size by ~90%)
- Backend: python:3.11-slim (minimal Python image)

### Resource Limits
Add to docker-compose.yml:
```yaml
backend:
  deploy:
    resources:
      limits:
        cpus: '1'
        memory: 512M
      reservations:
        cpus: '0.5'
        memory: 256M
```

## Security Best Practices

1. **Use secrets for sensitive data**
2. **Enable MongoDB authentication**
3. **Use HTTPS in production**
4. **Regularly update base images**
5. **Scan images for vulnerabilities**
```bash
docker scan fitlife-backend
docker scan fitlife-frontend
```

## Support

For issues with Docker deployment:
- Check this guide first
- Review Docker and Docker Compose documentation
- Open an issue on the project repository

---

**Happy Deploying! 🚀**
