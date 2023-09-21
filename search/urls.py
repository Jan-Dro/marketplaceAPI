from django.urls import path, register_converter
from .views import AllCategories, AllPost
from .converters import IntOrStrConverter, CategoryNameConverter
from . import views

register_converter(IntOrStrConverter, 'int_or_str')
register_converter(CategoryNameConverter, 'category_name') 


urlpatterns = [
    path('categories/', views.AllCategories.as_view(), name='all_categories'),
    path('categories/<int_or_str:category_id_or_name>/', views.AllCategories.as_view(), name='category_by_id_or_name'),
    path('categories/<category_name:category_id_or_name>/', views.AllCategories.as_view(), name='category_by_name'),
    path('categories/<int_or_str:category_id_or_name>/posts/', views.AllPost.as_view(), name='all_posts'),
    path('categories/<int_or_str:category_id_or_name>/posts/<int:post_id>/', views.AllPost.as_view(), name='get-post'),
]