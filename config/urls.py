from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from materials.views import MaterialViewSet
from listings.views import ListingViewSet
from exchanges.views import ExchangeRequestViewSet
from reviews.views import ReviewViewSet
from users.views import UserViewSet, RegisterView


router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'exchanges', ExchangeRequestViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),

    # API (chronione tokenem)
    path('api/', include(router.urls)),

    # API przeglądarkowe
    path('api-auth/', include('rest_framework.urls')),

    # AUTH (publiczne)
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/token/', obtain_auth_token),
]

