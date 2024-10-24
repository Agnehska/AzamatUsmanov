from django.urls import path
from .views import ServiceViewSet, BookingViewSet, ReviewViewSet, home, RegisterView, LoginView

urlpatterns = [
    path('', home, name='home'),
    path("services/", ServiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='service-list'),
    path("services/<int:pk>/", ServiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='service-detail'),
    path("bookings/", BookingViewSet.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path("bookings/<int:pk>/", BookingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='booking-detail'),
    path("reviews/", ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='review-list'),
    path("reviews/<int:pk>/", ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='review-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
