from django.urls import path 
from user import views


urlpatterns = [
    # path('register',views.SignupPage,name='user_register'),
    # path('login',views.login_view,name='user_login'),

    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),

#    path('logout', views.logout_user, name='logout'),
#     path('dashboard',views.dashboard_view,name='user_dashboard')

]
    