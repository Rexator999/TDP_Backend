from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.landingpage, name=""),
    path('clientlogin', views.clientloginpage, name="clientlogin"),
    path('clientregister', views.clientregisterpage, name="clientregister"),
    path('client1', views.clientpage1, name="client1"),
    path('client1_2', views.clientpage1_2, name="client1_2"),
    path('client2', views.clientpage2, name="client2"),
    path('sellerlogin', views.sellerloginpage, name="sellerlogin"),
    path('sellerregister', views.sellerregisterpage, name="sellerregister"),
    path('seller1', views.sellerpage1, name="seller1"),
    path('seller1_2', views.sellerpage1_2, name="seller1_2"),
    path('seller2', views.sellerpage2, name="seller2"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)