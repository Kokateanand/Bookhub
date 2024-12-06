from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('shop/', views.shop_view, name='shop'),
    path('product/<int:book_id>/', views.product_detail_view, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]
