from django.conf.urls import url
from django.contrib import admin

from guestbook.views import toppage


urlpatterns = [
    url(r'', toppage),
    url(r'^admin/', admin.site.urls),
]
