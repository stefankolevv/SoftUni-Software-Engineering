import os
import django
from main_app.validators import ValidationError
from main_app.models import Decimal

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Customer, Book, Product, DiscountedProduct, SpiderHero, FlashHero, Document

from django.contrib.postgres.search import SearchVector

# Create queries within functions