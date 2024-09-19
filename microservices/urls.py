from django.urls import path, include
from microservices.admin import services_admin_site
from microservices.views import home, services



urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('admin/', services_admin_site.urls),
]