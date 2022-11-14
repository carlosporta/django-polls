from django.contrib import admin
from django.urls import include, path


admin.site.site_header = 'Polls Administration'
admin.site.site_title  = 'Polls'
admin.site.index_title   = 'Polls'


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]