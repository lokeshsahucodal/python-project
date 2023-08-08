from .views import ProductViewSet
from rest_framework import routers
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]