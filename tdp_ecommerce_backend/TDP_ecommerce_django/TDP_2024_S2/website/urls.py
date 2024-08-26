from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.homepage, name=""),
    path('client', views.clientpage, name="client"),
    path('seller', views.sellerpage, name="seller"),
    path('test', views.testingpage, name="test"),
    path('imagesuccess/<int:image_id>/', views.imagesuccess, name="imagesuccess"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)