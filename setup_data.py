import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "craigslistMain.settings")
django.setup()

from search.models import Categories, Post

# Insert data into Categories model
categories_data = [
    {'category': 'Electronics'},
    {'category': 'Clothing'},
    {'category': 'Furniture'},
    {'category': 'Jewelry'},
    {'category': 'Sports Equipment'},
    {'category': 'Books'},
    {'category': 'Home Decor'},
    {'category': 'Toys'},
    {'category': 'Telecom'},
    {'category': 'Beauty Products'},
]

for data in categories_data:
    Categories.objects.create(category=data['category'])

print('Data has been inserted into the Categories model!')


category_data = [
    {'category_id': 1, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 2, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 3, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 4, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 5, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 6, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 7, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 8, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 9, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
        {'category_id': 10, 'post_data': [
        {'title': 'Vintage dress for sale', 'content': 'Minor cosmetic damage'},
        {'title': 'Electronics for sale', 'content': 'only used a few times'},
        {'title': 'Artwork for sale', 'content': 'works perfectly'},
        {'title': 'Vintage dress for sale', 'content': 'never used'},
        {'title': 'Electronics for sale', 'content': 'like new'},
    ]},
]

def insert_post_data(category_id, post_data):
    category = Categories.objects.get(pk=category_id)
    for data in post_data:
        Post.objects.create(category=category, **data)

for entry in category_data:
    insert_post_data(entry['category_id'], entry['post_data'])

print('Data has been inserted into the Post model!')