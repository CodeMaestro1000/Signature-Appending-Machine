from django.urls import path
from .views import HomePageView, RequestPageView, RequestSuccessView, RequestsView, HistoryView
from .views import accept_request, decline_request

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('make_request/', RequestPageView.as_view(), name='make_request'),
    path('request_sent/', RequestSuccessView.as_view(), name='request_sent'),
    path('requests/', RequestsView.as_view(), name='requests'),
    path('history/', HistoryView.as_view(), name='history'),
    path('requests/decline/<int:pk>/', decline_request, name='decline_request'),
    path('requests/accept/<int:pk>/', accept_request, name='accept_request'),
]