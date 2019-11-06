"""eventproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from event.views import home,signup,signin,signout,all_services,all_places,blog,aboutus,createplace,createservice,checkout,account,createblog,place,service
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<int:userid>/',home),
    path('signup/',signup),
    path('login/',signin),
    path('logout/',signout),
    path('services/<int:userid>/',all_services),
    path('places/<int:userid>/',all_places),
    path('aboutus/<int:userid>/',aboutus),
    path('createplace/<int:userid>/',createplace),
    path('createservice/<int:userid>/',createservice),
    path('checkout/<int:userid>/<int:bookid>/',checkout),
    path('account/<int:userid>/',account),
    path('blog/<int:userid>/',blog),
    path('createblog/<int:userid>/',createblog),
    path('place/<int:userid>/<int:placeid>/',place),
    path('service/<int:userid>/<int:serviceid>/',service),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
