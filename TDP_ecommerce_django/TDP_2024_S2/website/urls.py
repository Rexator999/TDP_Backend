from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import (
    ClientListCreateView, ClientDetailView, ClientRequestListCreateView, ClientRequestDetailView, ClientLoginView, ClientRegisterView, ClientHomeView,

    SellerListCreateView, SellerDetailView, SellerProductListCreateView, SellerProductDetailView,

)

urlpatterns = [
    

    path('logout/', views.logout, name='logout'),

    path('clientregister/', ClientRegisterView.as_view(), name='client_register'),
    path('clientlogin/', ClientLoginView.as_view(), name='client_login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('clienthome/', ClientHomeView.as_view(), name='clienthome'),

    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),

    path('client-requests/', ClientRequestListCreateView.as_view(), name='client-request-list-create'),
    path('client-requests/<int:pk>/', ClientRequestDetailView.as_view(), name='client-request-detail'),

    path('sellers/', SellerListCreateView.as_view(), name='seller-list-create'),
    path('sellers/<int:pk>/', SellerDetailView.as_view(), name='seller-detail'),

    path('seller-products/', SellerProductListCreateView.as_view(), name='seller-product-list-create'),
    path('seller-products/<int:pk>/', SellerProductDetailView.as_view(), name='seller-product-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)