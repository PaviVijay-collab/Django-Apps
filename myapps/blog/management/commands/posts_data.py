from blog.models import Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="This commands insert Post data"

    def handle(self, *args, **options):

        # DELETE EXISTING DATA
        Post.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully Deleted All Rows'))
    
        title = ['Latest Tech Trends in 2026', 
            'Healthy Living Tips', 
            'Top Travel Destinations', 
            'Delicious Homemade Recipes', 
            'Personal Finance Management', 
            'Modern Education System', 
            'Football Championship Highlights', 
            'Minimalist Lifestyle Guide', 
            'Fashion Trends This Year', 
            'Space Exploration Updates', 
            'Music Industry Evolution', 
            'Top Movies to Watch', 
            'Startup Business Ideas', 
            'Daily Motivation Boost', 
            'Home Workout Routines', 
            'Ancient History Facts', 
            'Modern Art Explained', 
            'Best Gaming Consoles', 
            'Global Political News', 
            'Nature Photography Guide']
        content = ['Technology is evolving rapidly with AI and automation.', 'Maintaining a balanced diet and regular exercise is key.', 'Explore the most beautiful places around the world.', 'Try these easy and tasty recipes at home.', 'Learn how to manage your finances effectively.', 'Online learning is reshaping education.', 'Latest updates from the football world.', 'How minimalism improves your life.', 'Explore trending fashion styles.', 'Discoveries beyond Earth.', 'How digital platforms changed music.', 'Best movies recommended this month.', 'Innovative business ideas for beginners.', 'Stay positive and focused on your goals.', 'Effective exercises you can do at home.', 'Learn about ancient civilizations.', 'Understanding contemporary art styles.', 'Top gaming devices in the market.', 'Latest updates in global politics.', 'Tips to capture stunning nature photos.']
        img_url = ['https://picsum.photos/seed/technology/800/400', 'https://picsum.photos/seed/health/800/400', 'https://picsum.photos/seed/travel/800/400', 'https://picsum.photos/seed/food/800/400', 'https://picsum.photos/seed/finance/800/400', 'https://picsum.photos/seed/education/800/400', 'https://picsum.photos/seed/sports/800/400', 'https://picsum.photos/seed/lifestyle/800/400', 'https://picsum.photos/seed/fashion/800/400', 'https://picsum.photos/seed/science/800/400', 'https://picsum.photos/seed/music/800/400', 'https://picsum.photos/seed/movies/800/400', 'https://picsum.photos/seed/business/800/400', 'https://picsum.photos/seed/motivation/800/400', 'https://picsum.photos/seed/fitness/800/400', 'https://picsum.photos/seed/history/800/400', 'https://picsum.photos/seed/art/800/400', 'https://picsum.photos/seed/gaming/800/400', 'https://picsum.photos/seed/politics/800/400', 'https://picsum.photos/seed/nature/800/400']
        category = ['tech', 'health', 'travel', 'food', 'finance', 'education', 'sports', 'lifestyle', 'fashion', 'science', 'music', 'movies', 'business', 'motivation', 'fitness', 'history', 'art', 'gaming', 'politics', 'nature']

        for title, content, img_url, category in zip(title, content, img_url, category):
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Successfully Inserted All Data in Rows")) 