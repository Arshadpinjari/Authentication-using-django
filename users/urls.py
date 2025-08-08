from django.urls import path
from .views import home, profile, RegisterView, CustomLogoutView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # Added logout URL
]
