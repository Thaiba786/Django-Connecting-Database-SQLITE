"""
URL configuration for ex6project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'<int:pk>/deletetab/'
# urls.py
# urls.py
# urls.py
# urls.py
from django.urls import path
from ex6app import views  # Import views from your app

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('read/', views.read, name='read'),
    path('<int:pk>/update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]





