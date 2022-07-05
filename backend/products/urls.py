from django.urls import path
from django.views import View

from . import views

# /api/products/
urlpatterns = [
    path('<int:pk>/', views.product_detail_view, name='product-detail'),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_destroy_view),
    path('',views.product_list_create_view, name='product-list')
]