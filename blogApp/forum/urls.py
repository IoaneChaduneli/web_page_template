from django.urls import path
from forum.views import home_view, about_view, contact_view, login_view

urlpatterns = [
    path('', home_view),
    path('about/', about_view),
    path('contact/', contact_view),
    path('loggin/', login_view)
]