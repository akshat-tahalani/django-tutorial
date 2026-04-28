from django.urls import path
from. import views

# every app has its own configuration 
urlpatterns =[
    path('hello/', views.say_hello),
    path('products/' ,views.product_list , name = 'product_list'),
    path('products/<int:id>/', views.product_detail ,name = 'product_detail'),
    path('products/slug/<slug:slug>/', views.product_detail_slug, name='product_detail_slug'),
    path('products/id/<int:id>', views.product_detail_id_redirect ,name = 'product_id_redirect'),
    path('contact/' , views.contact_view ,name = 'contact'),
    path('products/<slug:slug>/review/', views.add_review, name='add_review'),
]

# make sure to always end path routes with