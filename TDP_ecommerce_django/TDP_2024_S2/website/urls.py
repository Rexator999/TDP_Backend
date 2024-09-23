from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.landingpage, name=""),
    path('clientlogin', views.clientloginpage, name="clientlogin"),
    path('clientregister', views.clientregisterpage, name="clientregister"),
    path('client1', views.clientpage1, name="client1"),
    path('client2', views.clientpage2, name="client2"),
    path('sellerlogin', views.sellerloginpage, name="sellerlogin"),
    path('sellerregister', views.sellerregisterpage, name="sellerregister"),
    path('seller', views.sellerpage, name="seller"),
    path('imagesuccess/<int:image_id>/', views.imagesuccess, name="imagesuccess"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)