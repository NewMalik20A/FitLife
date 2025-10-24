// Mock data for fitness blog

export const blogPosts = [
  {
    id: '1',
    title: 'The Ultimate Guide to Building Muscle Mass',
    excerpt: 'Discover the science-backed strategies for maximizing muscle growth, from progressive overload to optimal nutrition timing.',
    content: 'Building muscle mass requires a combination of proper training, nutrition, and recovery...',
    category: 'Strength Training',
    author: 'Sarah Johnson',
    publishDate: '2025-08-15',
    readTime: '8 min read',
    image: 'https://images.unsplash.com/photo-1583454110551-21f2fa2afe61',
    featured: true
  },
  {
    id: '2',
    title: 'High-Intensity Interval Training: Maximize Your Cardio',
    excerpt: 'Learn how HIIT can transform your fitness routine with shorter, more effective workouts that burn fat and build endurance.',
    content: 'HIIT training has revolutionized the way we approach cardiovascular fitness...',
    category: 'Cardio',
    author: 'Mike Chen',
    publishDate: '2025-08-12',
    readTime: '6 min read',
    image: 'https://images.unsplash.com/photo-1599058917212-d750089bc07e',
    featured: true
  },
  {
    id: '3',
    title: 'Nutrition Basics: Fueling Your Fitness Journey',
    excerpt: 'Understanding macros, meal timing, and supplementation to support your training goals and optimize performance.',
    content: 'Proper nutrition is the foundation of any successful fitness program...',
    category: 'Nutrition',
    author: 'Emma Davis',
    publishDate: '2025-08-10',
    readTime: '10 min read',
    image: 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b',
    featured: false
  },
  {
    id: '4',
    title: 'Mastering the Mind-Muscle Connection',
    excerpt: 'Enhance your workout effectiveness by developing a stronger mental link with your physical movements.',
    content: 'The mind-muscle connection is often overlooked but critical for progress...',
    category: 'Training Tips',
    author: 'David Martinez',
    publishDate: '2025-08-08',
    readTime: '5 min read',
    image: 'https://images.unsplash.com/photo-1526506118085-60ce8714f8c5',
    featured: false
  },
  {
    id: '5',
    title: 'Recovery Strategies: The Missing Piece',
    excerpt: 'Why rest days matter and how to optimize recovery for consistent progress and injury prevention.',
    content: 'Recovery is when the magic happens - your body adapts and grows stronger...',
    category: 'Recovery',
    author: 'Sarah Johnson',
    publishDate: '2025-08-05',
    readTime: '7 min read',
    image: 'https://images.pexels.com/photos/2827392/pexels-photo-2827392.jpeg',
    featured: false
  },
  {
    id: '6',
    title: 'Functional Fitness: Training for Real Life',
    excerpt: 'Move beyond the machines and discover exercises that improve everyday movement patterns and quality of life.',
    content: 'Functional fitness focuses on movements that translate to daily activities...',
    category: 'Training Tips',
    author: 'Mike Chen',
    publishDate: '2025-08-03',
    readTime: '6 min read',
    image: 'https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg',
    featured: false
  },
  {
    id: '7',
    title: 'Powerlifting Fundamentals: Squat, Bench, Deadlift',
    excerpt: 'Master the big three compound movements that form the foundation of strength training programs.',
    content: 'The squat, bench press, and deadlift are the cornerstones of powerlifting...',
    category: 'Strength Training',
    author: 'David Martinez',
    publishDate: '2025-08-01',
    readTime: '9 min read',
    image: 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438',
    featured: false
  },
  {
    id: '8',
    title: 'Home Workouts: No Gym, No Problem',
    excerpt: 'Effective bodyweight exercises and minimal equipment routines you can do anywhere, anytime.',
    content: 'You don\'t need a fancy gym membership to stay fit and build strength...',
    category: 'Training Tips',
    author: 'Emma Davis',
    publishDate: '2025-07-28',
    readTime: '7 min read',
    image: 'https://images.pexels.com/photos/1552242/pexels-photo-1552242.jpeg',
    featured: false
  }
];

export const categories = [
  { id: 'all', name: 'All Articles', count: 8 },
  { id: 'strength-training', name: 'Strength Training', count: 2 },
  { id: 'cardio', name: 'Cardio', count: 1 },
  { id: 'nutrition', name: 'Nutrition', count: 1 },
  { id: 'training-tips', name: 'Training Tips', count: 3 },
  { id: 'recovery', name: 'Recovery', count: 1 }
];

export const featuredAuthors = [
  {
    name: 'Sarah Johnson',
    role: 'Certified Personal Trainer',
    bio: 'Specializing in strength training and body composition',
    articles: 2
  },
  {
    name: 'Mike Chen',
    role: 'HIIT Specialist',
    bio: 'Former track athlete and cardio conditioning expert',
    articles: 2
  },
  {
    name: 'Emma Davis',
    role: 'Nutritionist & Wellness Coach',
    bio: 'Helping athletes fuel their performance',
    articles: 2
  },
  {
    name: 'David Martinez',
    role: 'Powerlifting Coach',
    bio: 'Building strength through compound movements',
    articles: 2
  }
];

export const newsletterSignups = [];

export const getPostById = (id) => {
  return blogPosts.find(post => post.id === id);
};

export const getPostsByCategory = (category) => {
  if (category === 'all') return blogPosts;
  return blogPosts.filter(post => 
    post.category.toLowerCase().replace(' ', '-') === category
  );
};

export const getFeaturedPosts = () => {
  return blogPosts.filter(post => post.featured);
};

export const subscribeToNewsletter = (email) => {
  newsletterSignups.push({ email, date: new Date().toISOString() });
  return true;
};