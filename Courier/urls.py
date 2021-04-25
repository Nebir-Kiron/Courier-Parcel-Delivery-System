from django.urls import path
from .import views


urlpatterns = [
    path('', views.home_Page, name='homePage'),
    path('dashboard/', views.dashboard_Page, name='dashboardPage'),
    path('customer/', views.customer_Page, name='customerPage'),
    path('product/', views.products_Page, name='productPage'),
]
