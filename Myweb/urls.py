"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from portfolio import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header="Developer desk"
admin.site.site_title="Portfolio"
admin.site.index_title="Welcome Developer"

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Portfolio
    path('',views.home,name='home'),
    path('resume',views.Resume_view,name='resume'),
    path('projects',views.projects_view,name='projects'),
    path('certifications',views.certifications_view,name='certifications_view'),
    path('achievements',views.Achievements_view,name='Achievements_view'),
    path('blogs',views.Blog_view,name='Blogs_view'),
    path('contacts',views.contact_view,name='contact_view')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
