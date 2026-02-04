from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from materials.views import MaterialViewSet
from listings.views import ListingViewSet
from exchanges.views import ExchangeRequestViewSet
from reviews.views import ReviewViewSet
from users.views import UserViewSet


router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'exchanges', ExchangeRequestViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # ← TEN WIERSZ JEST KLUCZOWY
]
