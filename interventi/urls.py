from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from interventi import views
# from gse.dispositivi import toolbox



urlpatterns = [
    # Examples:
    # url(r'^$', 'gse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin_tools/', include('admin_tools.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')), # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    # url(r'^admin/', admin.site.urls),

    path('get_Asset/', views.get_Asset),

               ]

