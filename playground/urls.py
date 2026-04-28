from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

# every app has its own configuration 
urlpatterns =[
    path('hello/', views.say_hello),
    path('products/' ,views.product_list , name = 'product_list'),
    path('products/<int:id>/', views.product_detail ,name = 'product_detail'),
    path('products/slug/<slug:slug>/', views.product_detail_slug, name='product_detail_slug'),
    path('products/id/<int:id>', views.product_detail_id_redirect ,name = 'product_id_redirect'),
    path('contact/' , views.contact_view ,name = 'contact'),
    path('products/<slug:slug>/review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('products/create/', views.create_product, name='create_product'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# make sure to always end path routes with