from django.core.management.base import BaseCommand
from blog.models import Category


class Command(BaseCommand):
    help = "This Command Insert Categories Data"

    def handle(self, *args, **options):
        categories = ['general', 
                      'tech', 
                    'health', 
                    'travel', 
                    'food', 
                    'finance', 
                    'education', 
                    'sports', 
                    'lifestyle', 
                    'fashion', 
                    'science', 
                    'music', 
                    'movies', 
                    'business', 
                    'motivation', 
                    'fitness', 
                    'history', 
                    'art', 
                    'gaming', 
                    'politics', 
                    'nature']
        
        # DELETE EXISTING DATA
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Data Deleted Successfully'))

        for name in categories:
            # INSERTING DATA
            Category.objects.create(name=name)

        self.stdout.write(self.style.SUCCESS('Inserted Successfully'))