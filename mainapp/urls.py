from django.urls import path, include
from . import views

urlpatterns = [
    # for default route to main app ie djangosite/myappp route
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('contact/<str:name>', views.contactme, name="contactme"),

    path('', views.index, name="dashboard"),
    path('create_post', views.createPost, name="create_post"),
    path('delete_post/<int:post_id>', views.deletePost, name="delete_post"),

]
