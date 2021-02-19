"""ACS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "home_page" ),

    # about page
    path('about/', views.about, name = "about_page" ),
    path('about/President', views.president, name = "president" ),
    path('about/Founder', views.founder, name = "founder" ),
    path('about/Secratary', views.secratary, name = "secratary" ),

    # base navigator
    path('', include(('college.urls', 'college'), namespace='college')),
    path('', include(('hospital.urls', 'hospital'), namespace='hospital')),

    # contact us
    path('contact-us/', views.contact, name = "contact-us" ),

    #admission
    path('admission/', views.admission, name = "admission" ),

    # accrediations

    path('acc1/', views.acc1, name = "acc1" ),
    path('acc2/', views.acc2, name = "acc2" ),
    path('acc3/', views.acc3, name = "acc3" ),



    
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
