from django.urls import path, include
from . import views
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns = [
    path('restapi/', include(router.urls)),
]
