from django.conf.urls import include, url
from django.contrib import admin
 
urlpatterns = [
    url(r'^sales-mail-structured/', include('sales-mail-structured.urls', namespace='sales-mail-structured')),
    url(r'^admin/', admin.site.urls),
]