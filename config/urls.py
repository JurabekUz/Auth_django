
from django.contrib import admin
from django.urls import path, include
from accounts.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),

    path('', Home, name='home')
]
