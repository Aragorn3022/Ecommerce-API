
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiUsers/', include('users.urls')),
    path('apiProducts/', include('productsApi.urls')),

]
