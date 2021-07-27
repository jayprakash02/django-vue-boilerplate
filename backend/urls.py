"""URL Configuration"""

from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from .api.views import index_view

router = routers.DefaultRouter()

urlpatterns = [
    
    path('', index_view, name='index'),
    path('api/admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
