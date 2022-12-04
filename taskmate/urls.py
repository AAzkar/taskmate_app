from django.contrib import admin
from django.urls import path, include
from todolist_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('task/', include('todolist_app.urls')),
    path('account/', include('users_app.urls')),
    path('about-us', views.about, name='about'),
    path('contact-us', views.contact, name='contact'),
]
