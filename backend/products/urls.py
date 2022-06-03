from django.urls import path

from . import views

# /api/products/
urlpatterns = [
    path("<int:pk>/", views.product_detail_view),
    path('', views.product_create_view)
]