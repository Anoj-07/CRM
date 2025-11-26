from django.urls import path
from .views import LeadApiView, LeadDetailViewAPI, CompanyApiView, CompanyDetailApiView

urlpatterns = [
    path('lead/', LeadApiView.as_view(), name='lead-list-create'),
    path('lead/<int:lead_id>/', LeadDetailViewAPI.as_view(), name='lead-detail'),
    path("company/", CompanyApiView.as_view(), name="company-list-create"),
    path("company/<int:company_id>/", CompanyDetailApiView.as_view(), name="company-detail")
]