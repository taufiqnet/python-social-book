from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import hello_world

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('hra/', include('hra.urls')),
    path('invoices/', include('invoices.urls', namespace='invoices')),
    #path('invoices/', hello_world)
]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Change the Admin Panel Header
admin.site.site_header = "Invoice Admin System"
admin.site.index_title = "Management"