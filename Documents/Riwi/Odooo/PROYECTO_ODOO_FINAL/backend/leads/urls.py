from django.urls import path
from .views import LeadList

urlpatterns = [
    path('leads/', LeadList.as_view(), name='leads-list'),
]