from django.conf.urls import include, url
from django.contrib import admin
 
urlpatterns = [
    path(r'^sales-mail-structured/', include('sales-mail-structured.urls', namespace='sales-mail-structured')),
    path(r'^admin/', admin.site.urls),
]