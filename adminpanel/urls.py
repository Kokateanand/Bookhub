
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('categories/', views.categories, name='categories'),
    path('customers/', views.customers, name='customers'),
    path('warehouses/', views.warehouses, name='warehouses'),

   
    path('login/',views.login_view,name='admin_login'),
    path('logout/',views.logout_view,name='admin_logout')
    

]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




