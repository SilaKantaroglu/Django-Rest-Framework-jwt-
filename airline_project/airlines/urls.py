from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import UserCreate,UserList, AirlineListView, UserDetail, AirlineListCreateView, AirlineRetrieveUpdateDestroyAPIView,AircraftListView,AircraftListCreateView, AircraftRetrieveUpdateDestroyAPIView

urlpatterns = [

    #USERS URLS
    path('registration/', UserCreate.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/',UserDetail.as_view()),


    #AİRLİNES URLS
    path('airlines/', AirlineListView.as_view()),
    path('airline/', AirlineListCreateView.as_view()),
    path('airline/<int:pk>', 
    AirlineRetrieveUpdateDestroyAPIView.as_view()),

    #AİRCRAFTS URLS
    path('aircrafts/', AircraftListView.as_view()),
    path('aircraft/', AircraftListCreateView.as_view()),
    path('aircraft/<int:pk>', AircraftRetrieveUpdateDestroyAPIView.as_view()),

    #TOKEN URLS
    path('api-token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]