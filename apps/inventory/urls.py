from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, InventoryLogViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet)
router.register(r'logs', InventoryLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
