from django.contrib import admin
from django.urls import path, include
from warehouse.views import OrderViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'order', OrderViewSet)  # pattern for URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),  # http://127.0.0.1:8001/api/v1/order/ and http://127.0.0.1:8001/api/v1/order/{str:slug}/
]
