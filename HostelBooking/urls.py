from django.contrib import admin
from django.urls import path, include

from HostelApp.views import Room_View, Booking_View
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'room', Room_View)
router.register(r'booking', Booking_View)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/room/<int:pk>/', Room_View.as_view({'get': 'retrieve'}), name='room-detail'),
    path('api/booking/<int:pk>/', Booking_View.as_view({'get': 'retrieve'}), name='booking-detail'),
]

