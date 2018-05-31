from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from prestiti import views
# from gse.dispositivi import toolbox



urlpatterns = [
    # Examples:
    # url(r'^$', 'gse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin_tools/', include('admin_tools.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^select2/', include('django_select2.urls')),
    # url(r'^toolbox/',  'dispositivi.toolbox'),
    # url(r'^filer/', include('filer.urls')),
    # path('get_Prestiti_Produttore/',  views.get_Prestiti_Produttore),
    # path('get_Prestiti_Modello/', views.get_Prestiti_Modello),


               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # qui si configura correttamente il reverse della cartella MEDIA

