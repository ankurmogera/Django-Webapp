from django.urls import path, include
from security.views import registerUser
from django.contrib.auth import views



urlpatterns = [
    path('register-user/', registerUser, name='registerUser'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='index'), name='logout'),
    path('contacts/', include('contacts.urls')),
]
