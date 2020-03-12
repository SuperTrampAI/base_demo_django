"""base_demo_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from base_app import views
from base_demo_django import settings
from vote import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/',views.index)
    path("base_app2/",include('base_app2.urls')),
    path('vote/',include('vote.urls')),
    path('vote/teachers/', views.show_teachers),
    path('vote/praise/', views.prise_or_criticize),
    path('vote/criticize/', views.prise_or_criticize),

]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns.insert(0, path('__debug__/', include(debug_toolbar.urls)))



