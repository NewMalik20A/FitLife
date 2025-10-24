import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Sample articles data
articles = [
    {
        'id': '1',
        'title': 'The Ultimate Guide to Building Muscle Mass',
        'excerpt': 'Discover the science-backed strategies for maximizing muscle growth, from progressive overload to optimal nutrition timing.',
        'content': 'Building muscle mass requires a combination of proper training, nutrition, and recovery. This comprehensive guide will walk you through everything you need to know to achieve your fitness goals effectively and sustainably.',
        'category': 'Strength Training',
        'author': 'Sarah Johnson',
        'publishDate': datetime(2025, 8, 15),
        'readTime': '8 min read',
        'image': 'https://images.unsplash.com/photo-1583454110551-21f2fa2afe61',
        'featured': True,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '2',
        'title': 'High-Intensity Interval Training: Maximize Your Cardio',
        'excerpt': 'Learn how HIIT can transform your fitness routine with shorter, more effective workouts that burn fat and build endurance.',
        'content': 'HIIT training has revolutionized the way we approach cardiovascular fitness. By alternating between high-intensity bursts and recovery periods, you can achieve better results in less time.',
        'category': 'Cardio',
        'author': 'Mike Chen',
        'publishDate': datetime(2025, 8, 12),
        'readTime': '6 min read',
        'image': 'https://images.unsplash.com/photo-1599058917212-d750089bc07e',
        'featured': True,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '3',
        'title': 'Nutrition Basics: Fueling Your Fitness Journey',
        'excerpt': 'Understanding macros, meal timing, and supplementation to support your training goals and optimize performance.',
        'content': 'Proper nutrition is the foundation of any successful fitness program. Learn how to fuel your body for optimal performance and recovery.',
        'category': 'Nutrition',
        'author': 'Emma Davis',
        'publishDate': datetime(2025, 8, 10),
        'readTime': '10 min read',
        'image': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b',
        'featured': False,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '4',
        'title': 'Mastering the Mind-Muscle Connection',
        'excerpt': 'Enhance your workout effectiveness by developing a stronger mental link with your physical movements.',
        'content': 'The mind-muscle connection is often overlooked but critical for progress. Discover techniques to improve your focus and maximize every rep.',
        'category': 'Training Tips',
        'author': 'David Martinez',
        'publishDate': datetime(2025, 8, 8),
        'readTime': '5 min read',
        'image': 'https://images.unsplash.com/photo-1526506118085-60ce8714f8c5',
        'featured': False,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '5',
        'title': 'Recovery Strategies: The Missing Piece',
        'excerpt': 'Why rest days matter and how to optimize recovery for consistent progress and injury prevention.',
        'content': 'Recovery is when the magic happens - your body adapts and grows stronger. Learn the best strategies to maximize your recovery.',
        'category': 'Recovery',
        'author': 'Sarah Johnson',
        'publishDate': datetime(2025, 8, 5),
        'readTime': '7 min read',
        'image': 'https://images.pexels.com/photos/2827392/pexels-photo-2827392.jpeg',
        'featured': False,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '6',
        'title': 'Functional Fitness: Training for Real Life',
        'excerpt': 'Move beyond the machines and discover exercises that improve everyday movement patterns and quality of life.',
        'content': 'Functional fitness focuses on movements that translate to daily activities. Build strength that matters in real life.',
        'category': 'Training Tips',
        'author': 'Mike Chen',
        'publishDate': datetime(2025, 8, 3),
        'readTime': '6 min read',
        'image': 'https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg',
        'featured': False,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '7',
        'title': 'Powerlifting Fundamentals: Squat, Bench, Deadlift',
        'excerpt': 'Master the big three compound movements that form the foundation of strength training programs.',
        'content': 'The squat, bench press, and deadlift are the cornerstones of powerlifting. Learn proper form and technique for maximum gains.',
        'category': 'Strength Training',
        'author': 'David Martinez',
        'publishDate': datetime(2025, 8, 1),
        'readTime': '9 min read',
        'image': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438',
        'featured': False,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    },
    {
        'id': '8',
        'title': 'Home Workouts: No Gym, No Problem',
        'excerpt': 'Effective bodyweight exercises and minimal equipment routines you can do anywhere, anytime.',
        'content': 'You don\\'t need a fancy gym membership to stay fit and build strength. Discover effective home workout strategies.',
        'category': 'Training Tips',
        'author': 'Emma Davis',
        'publishDate': datetime(2025, 7, 28),
        'readTime': '7 min read',
        'image': 'https://images.pexels.com/photos/1552242/pexels-photo-1552242.jpeg',
        'featured': False,
        'createdAt': datetime.utcnow(),
        'updatedAt': datetime.utcnow()
    }
]

async def seed_database():
    # Connect to MongoDB
    mongo_url = os.environ['MONGO_URL']
    client = AsyncIOMotorClient(mongo_url)
    db = client[os.environ['DB_NAME']]
    
    try:
        # Clear existing data
        await db.articles.delete_many({})
        print("Cleared existing articles")
        
        # Insert articles
        await db.articles.insert_many(articles)
        print(f"Successfully seeded {len(articles)} articles")
        
        # Create indexes
        await db.articles.create_index("id", unique=True)
        await db.articles.create_index("category")
        await db.articles.create_index("featured")
        await db.newsletter_subscribers.create_index("email", unique=True)
        print("Created database indexes")
        
        print("Database seeding completed!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(seed_database())
