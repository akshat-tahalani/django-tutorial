from django.core.management.base import BaseCommand
from playground.models import Product, Category, Tag


class Command(BaseCommand):
    help = 'Populate database with sample e-commerce data'

    def handle(self, *args, **options):
        # Create categories
        electronics, _ = Category.objects.get_or_create(name='Electronics')
        fashion, _ = Category.objects.get_or_create(name='Fashion')
        home, _ = Category.objects.get_or_create(name='Home & Garden')
        sports, _ = Category.objects.get_or_create(name='Sports')

        # Create tags
        new, _ = Tag.objects.get_or_create(name='New')
        sale, _ = Tag.objects.get_or_create(name='Sale')
        bestseller, _ = Tag.objects.get_or_create(name='Bestseller')
        eco_friendly, _ = Tag.objects.get_or_create(name='Eco-friendly')

        # Products data
        products_data = [
            {
                'title': 'Wireless Bluetooth Headphones',
                'price': 79.99,
                'description': 'High-quality wireless headphones with noise cancellation and 30-hour battery life.',
                'category': electronics,
                'size': 'M',
                'inventory': 50,
                'is_available': True,
                'tags': [new, bestseller]
            },
            {
                'title': 'Premium Leather Jacket',
                'price': 199.99,
                'description': 'Stylish genuine leather jacket perfect for any occasion.',
                'category': fashion,
                'size': 'L',
                'inventory': 25,
                'is_available': True,
                'tags': [sale]
            },
            {
                'title': 'Yoga Mat Premium',
                'price': 39.99,
                'description': 'Non-slip yoga mat made from eco-friendly materials, 6mm thickness.',
                'category': sports,
                'size': 'S',
                'inventory': 100,
                'is_available': True,
                'tags': [eco_friendly, bestseller]
            },
            {
                'title': 'Smart Watch Series 5',
                'price': 249.99,
                'description': 'Advanced fitness tracking with heart rate monitor and water resistance.',
                'category': electronics,
                'size': 'S',
                'inventory': 35,
                'is_available': True,
                'tags': [new]
            },
            {
                'title': 'Organic Coffee Beans',
                'price': 24.99,
                'description': 'Single-origin organic coffee beans from Ethiopia, 1kg bag.',
                'category': home,
                'size': 'M',
                'inventory': 200,
                'is_available': True,
                'tags': [eco_friendly, bestseller]
            },
            {
                'title': 'LED Desk Lamp',
                'price': 49.99,
                'description': 'Adjustable LED desk lamp with USB charging port and touch controls.',
                'category': home,
                'size': 'M',
                'inventory': 60,
                'is_available': True,
                'tags': [new, sale]
            },
            {
                'title': 'Running Shoes Pro',
                'price': 129.99,
                'description': 'Professional running shoes with gel cushioning technology.',
                'category': sports,
                'size': 'L',
                'inventory': 45,
                'is_available': True,
                'tags': [bestseller]
            },
            {
                'title': 'Casual Cotton T-Shirt',
                'price': 19.99,
                'description': '100% organic cotton t-shirt, breathable and comfortable.',
                'category': fashion,
                'size': 'M',
                'inventory': 150,
                'is_available': True,
                'tags': [eco_friendly, sale]
            },
        ]

        # Create products
        for product_data in products_data:
            tags = product_data.pop('tags')
            product, created = Product.objects.get_or_create(
                title=product_data['title'],
                defaults=product_data
            )
            if created:
                product.tags.set(tags)
                self.stdout.write(self.style.SUCCESS(f'Created: {product.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Already exists: {product.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully populated database!'))
