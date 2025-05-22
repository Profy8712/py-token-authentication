from django.urls import path
from users.views import RegisterUserView, LoginUserView, ManageUserView

app_name = "users"

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('me/', ManageUserView.as_view(), name='me'),
]
