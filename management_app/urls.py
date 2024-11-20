from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet,StudentViewSet,SubjectViewSet

#creating a router to register the viewsets
router = DefaultRouter()
router.register(r'faculties',FacultyViewSet)
router.register(r'students',StudentViewSet)
router.register(r'subjects', SubjectViewSet)

#to prefix all the endpoints with 'api/'
urlpatterns = [
    path('api/', include(router.urls)), 
]