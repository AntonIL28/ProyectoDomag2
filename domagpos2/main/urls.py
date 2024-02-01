from django.urls import path, include
from . import views
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'Task', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.Home, name='home'),

]
