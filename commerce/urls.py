
from django.contrib import admin
from django.urls import include, path
from commerce import settings
from django.conf.urls.static import static
from commerce.settings import MEDIA_ROOT
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name="home"),
    path('mystore/',include('mystore.urls')),
    path('cart/',include('cart.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
