import random

from blog.models import Post, Category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help="This commands insert Post data"


    def handle(self, *args, **options):

        # DELETE EXISTING DATA
        Post.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Successfully Deleted All Rows'))
    
        title = ['The Power of Daily Habits', 
                 'Time Management for Busy People', 
                 'Why Reading Improves Thinking', 
                 'Building Self-Discipline', 
                 'The Importance of Networking', 
                 'Top 5 Healthy Breakfast Ideas', 
                 'Benefits of Drinking Warm Water', 
                 'Homemade Pizza Recipe Guide', 
                 'Understanding Balanced Diet', 
                 'Importance of Hydration', 
                 'Rise of Esports Industry', 
                 'Best Strategy Games in 2026', 
                 'Gaming PC Setup Guide', 
                 'Mobile Gaming Trends', 
                 'Tips to Improve Reaction Time', 
                 'Minimalist Wardrobe Essentials', 
                 'Summer Fashion Trends 2026', 
                 'Choosing the Right Footwear', 
                 'Formal vs Casual Styling', 
                 'Sustainable Clothing Choices', 
                 'Importance of Online Learning', 
                 'Effective Study Techniques', 
                 'Role of Technology in Classrooms', 
                 'Why Critical Thinking Matters', 
                 'Career-Oriented Courses in 202']
        content = ['Small daily habits create long-term success. Consistency matters more than intensity in achieving life goals.', 'Effective time management improves productivity and reduces stress in both personal and professional life.', 'Reading regularly enhances vocabulary, imagination, and analytical thinking skills.', 'Self-discipline helps you stay focused and achieve goals despite distractions and challenges.', 'Networking builds valuable connections that can open doors to new opportunities.', 'Healthy breakfasts like oats, fruits, and eggs provide energy and improve concentration.', 'Warm water improves digestion and boosts metabolism when consumed daily.', 'Making pizza at home allows customization with fresh ingredients and flavors.', 'A balanced diet includes proteins, carbohydrates, fats, vitamins, and minerals.', 'Drinking enough water daily improves skin health and body performance.', 'Esports has grown into a billion-dollar industry with global tournaments.', 'Strategy games challenge critical thinking and decision-making skills.', 'A powerful GPU and sufficient RAM are essential for smooth gaming performance.', 'Mobile games are becoming more advanced with improved graphics and multiplayer modes.', 'Practicing regularly and maintaining focus helps improve gaming reaction speed.', 'A minimalist wardrobe includes versatile pieces that match multiple outfits.', 'Light fabrics and pastel colors dominate summer fashion trends.', 'Comfort and style both matter when selecting daily footwear.', 'Understanding dress codes helps maintain professionalism and personal style.', 'Eco-friendly fashion reduces environmental impact and promotes sustainability.', 'Online education provides flexibility and accessibility to students worldwide.', 'Active recall and spaced repetition improve long-term memory retention.', 'Technology enhances interactive learning and student engagement.', 'Critical thinking enables better problem-solving and decision-making skills.', 'Skill-based courses help students stay competitive in evolving industries.']
        img_url = ['https://picsum.photos/seed/general1/800/400', 'https://picsum.photos/seed/general2/800/400', 'https://picsum.photos/seed/general3/800/400', 'https://picsum.photos/seed/general4/800/400', 'https://picsum.photos/seed/general5/800/400', 'https://picsum.photos/seed/food1/800/400', 'https://picsum.photos/seed/food2/800/400', 'https://picsum.photos/seed/food3/800/400', 'https://picsum.photos/seed/food4/800/400', 'https://picsum.photos/seed/food5/800/400', 'https://picsum.photos/seed/gaming1/800/400', 'https://picsum.photos/seed/gaming2/800/400', 'https://picsum.photos/seed/gaming3/800/400', 'https://picsum.photos/seed/gaming4/800/400', 'https://picsum.photos/seed/gaming5/800/400', 'https://picsum.photos/seed/fashion1/800/400', 'https://picsum.photos/seed/fashion2/800/400', 'https://picsum.photos/seed/fashion3/800/400', 'https://picsum.photos/seed/fashion4/800/400', 'https://picsum.photos/seed/fashion5/800/400', 'https://picsum.photos/seed/education1/800/400', 'https://picsum.photos/seed/education2/800/400', 'https://picsum.photos/seed/education3/800/400', 'https://picsum.photos/seed/education4/800/400', 'https://picsum.photos/seed/education5/800/400']

        def find_categories(title, categories):
            for category in categories:
                words = title.lower().split()
                if category.name in words:
                    return category     
            return categories[0]

        categories = Category.objects.all()
        for title, content, img_url in zip(title, content, img_url):
            category = find_categories(title, categories)

            # INSERTING DATA
            Post.objects.create(title=title, content=content, img_url=img_url, category=category)

        self.stdout.write(self.style.SUCCESS("Successfully Inserted All Data in Rows")) 
    
    



