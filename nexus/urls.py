from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from dashboard.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
