from django.urls import path
from emailer import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.SendEmailView.as_view(), name="send_email"),
]
urlpatterns += staticfiles_urlpatterns()
