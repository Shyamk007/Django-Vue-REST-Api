from django.urls import path
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students',StudentViewSet)

# urlpatterns = [
#     path('students/',index)
# ]
# since we have implemented the rest_framework we no longer
# need the path('students/',index instead we will use the method that we have just declared below)

# this was the method to do the backend now we have a successfully running api we can do the frontend
urlpatterns = router.urls