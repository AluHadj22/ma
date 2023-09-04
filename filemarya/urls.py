from django.contrib import admin
from django.urls import include, path
from django.urls import path
from filemarya import views
from django.conf import settings
from django.conf.urls.static import static
from django_downloadview import ObjectDownloadView
from filemarya.models import Data
from django.shortcuts import render
download = ObjectDownloadView.as_view(model=Data, file_field=
'file')

def home(request):
   return render(request, 'templates/home.html')

urlpatterns = [
    path('', views.home, name="home"),
    path('download/', download, name="download"),
    path('admin/', admin.site.urls),
    path('filer/', include('filer.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)