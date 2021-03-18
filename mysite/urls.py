"""mysite URL Configuration

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
from django.urls import include, path

urlpatterns = [
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]

"""최상위 url에서 url을 파싱하고 받아서 path 별로 다른앱으로 분기 시켜줌
앱이 여러개있으면, url에 따라서 파싱을 해주고 path에 앱으로 분기시켜주는 것"""

