from django.urls import path
from customer import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("login/",views.SignInView.as_view(),name="signin"),
    path("home/",views.IndexView.as_view(),name="index"),
    path("profile/",views.CreateProfileView.as_view(),name="profile-detail"),
    path("profile/<int:id>/change",views.ProfileUpdateView.as_view(),name="profile-update"),
    path("profile/<int:id>/remove",views.ProfileDeletelView.as_view(),name="profile-delete"),
    path("logout/",views.SignOutView.as_view(),name="signout"),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

