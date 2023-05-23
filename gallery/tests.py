from django.test import TestCase

from django.test import TestCase
from .models import Image, Category
from datetime import date

class CategoryModelTest(TestCase):
    def test_name_field(self):
        category = Category(name='Test Category')
        category.save()
        saved_category = Category.objects.get(pk=category.pk)
        self.assertEqual(saved_category.name, 'Test Category')

class ImageModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Nature')
        self.image = Image.objects.create(
            title='Beautiful Landscape',
            image='path/to/image.jpg',
            created_date=date.today(),
            age_limit=18
        )
        self.image.categories.add(self.category)

    def test_image_title(self):
        self.assertEqual(self.image.title, 'Beautiful Landscape')

    def test_image_categories(self):
        self.assertEqual(self.image.categories.count(), 1)
        self.assertEqual(self.image.categories.first(), self.category)

    def test_image_created_date(self):
        self.assertEqual(self.image.created_date, date.today())

    def test_image_age_limit(self):
        self.assertEqual(self.image.age_limit, 18)

