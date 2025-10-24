from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
import uuid

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    excerpt: str
    content: str
    category: str
    author: str
    publishDate: datetime
    readTime: str
    image: str
    featured: bool = False
    createdAt: datetime = Field(default_factory=datetime.utcnow)
    updatedAt: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Ultimate Guide to Building Muscle Mass",
                "excerpt": "Discover the science-backed strategies...",
                "content": "Building muscle mass requires...",
                "category": "Strength Training",
                "author": "Sarah Johnson",
                "publishDate": "2025-08-15T00:00:00Z",
                "readTime": "8 min read",
                "image": "https://example.com/image.jpg",
                "featured": True
            }
        }

class ArticleCreate(BaseModel):
    title: str
    excerpt: str
    content: str
    category: str
    author: str
    publishDate: datetime
    readTime: str
    image: str
    featured: bool = False

class ArticleUpdate(BaseModel):
    title: Optional[str] = None
    excerpt: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    author: Optional[str] = None
    publishDate: Optional[datetime] = None
    readTime: Optional[str] = None
    image: Optional[str] = None
    featured: Optional[bool] = None

class Category(BaseModel):
    id: str
    name: str
    count: int = 0

class NewsletterSubscriber(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    email: EmailStr
    subscribedAt: datetime = Field(default_factory=datetime.utcnow)

class NewsletterSubscribe(BaseModel):
    email: EmailStr