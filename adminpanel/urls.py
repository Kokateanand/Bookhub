from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    # Categories
    path('categories/', views.categories, name='categories'),
    path('categories/add/', views.add_category, name='add_category'),

    # Authors
    path('authors/', views.authors, name='authors'),
    path('authors/add/', views.add_author, name='add_author'),

    # Books
    path('books/', views.books, name='books'),
    path('books/add/', views.add_book, name='add_book'),

    # Warehouses
    path('warehouses/', views.warehouses, name='warehouses'),
    path('warehouses/add/', views.add_warehouse, name='add_warehouse'),

    
    path('customers/', views.customers, name='customers'),
    path('customers/add/', views.add_customer, name='add_customer'),

    path('update/<int:id>/', views.update_customer, name='update_customer'),
    # path('delete/<int:id>/', views.delete_customer, name='delete_customer'),
    path('update/<int:id>/', views.update_category, name='update_category'),
    path('update/author/<int:id>/', views.update_author, name='update_author'),
    path('update/warehouse/<int:id>/', views.update_warehouse, name='update_warehouse'),
     path('update/<int:id>/', views.update_book, name='update_book'),
     

]
