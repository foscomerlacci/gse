from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from dispositivi import views as dispositivi_views
from interventi import views as interventi_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns      # indispensabile per i file statici serviti da gunicorn
# from gse.dispositivi import toolbox



urlpatterns = [
    # path('admin/dispositivi/', include('dispositivi.urls')),
    # path('admin/interventi/', include('interventi.urls')),
    # Examples:
    # url(r'^$', 'gse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^dispositivi/', include('dispositivi.urls')),
    # url(r'^interventi/', include('interventi.urls')),
    # url(r'^admin_tools/', include('admin_tools.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    # url(r'^select2/', include('django_select2.urls')),
    # url(r'^toolbox/',  'dispositivi.toolbox'),
    # url(r'^filer/', include('filer.urls')),
    path('get_Produttore/',  dispositivi_views.get_Produttore),
    path('get_Modello/', dispositivi_views.get_Modello),
    path('get_Asset/', interventi_views.get_Asset),


               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # qui si configura correttamente il reverse della cartella MEDIA

urlpatterns += staticfiles_urlpatterns()    # indispensabile per i file statici serviti da gunicorn

admin.site.site_url = None
admin.site.site_header = ('Gestione Supporto Enhanced')
# admin.site.site_title = ('Gestione Supporto Enhanced')
# admin.site.index_title = ('Gestione Supporto Enhanced')



