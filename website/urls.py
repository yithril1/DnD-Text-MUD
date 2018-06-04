"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include
from game import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('char_create', views.char_create, name="creation"),
    url(r'^get_guild_info$', views.get_guild_info),
    url(r'^get_race_info$', views.get_race_info),
    url(r'^get_subraces$', views.get_subraces),
    url(r'^get_subrace_stats$', views.get_subrace_stats),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^get_background_info', views.get_background_info),
    url(r'^get_skill_proficiencies', views.get_skill_proficiencies),
    path('', include('pages.urls')),
    path('users/', include('users.urls')),  # new
    path('accounts/', include('allauth.urls')),
    url(r'^post_character$', views.post_character)

]
