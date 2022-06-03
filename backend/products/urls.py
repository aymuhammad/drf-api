from django.urls import path
from django.views import View

from . import views

# /api/products/
urlpatterns = [
    path("<int:pk>/", views.product_detail_view),
    # path('', views.product_create_view),
    path('', views.product_list_create_view)
]