from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ZerodhaApi.urls')),
    path('', include('ReactDashboardApi.urls')),
    path('', include('AIBot.urls')),
    path('', include('AdRevenue.urls'))
]
