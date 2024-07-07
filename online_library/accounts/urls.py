from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = "accounts"
urlpatterns = [
    path("signup/",views.SignUp.as_view(),name="signup"),
    path("logout/",views.logout_user,name="logout"),
    path("login/",views.loginuser, name="login"),
    path("become_an_uploader/",views.CreateUploader.as_view(),name="createuploader")
]
