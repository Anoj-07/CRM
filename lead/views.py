from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import LeadSerializer, CompanySerializer
from .models import Lead, Company
from config import global_parameter as gp
# Create your views here.

# API for Lead [GET, POST]
class LeadApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            leads = Lead.objects.filter(is_delete=False)
            serializer = LeadSerializer(leads, many=True)
            msg = {
                gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                gp.RESPONSE_KEY : gp.RESPONSE_OK_MSG,
                gp.DATA : serializer.data
            }
            return Response(msg, status=status.HTTP_200_OK)
        except Exception as e:
            msg={
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = LeadSerializer(data=request.data, context={"request": request})
            if serializer.is_valid():
                serializer.save()
                msg = {
                    gp.RESPONSE_CODE_KEY: gp.SUCCESS_CODE,
                    gp.RESPONSE_KEY: gp.RESPONSE_SUCCESS_MSG,
                    gp.DATA: serializer.data
                }
                return Response(msg, status=status.HTTP_201_CREATED)
            msg = {
                gp.RESPONSE_CODE_KEY: gp.UNSUCCESS_CODE,
                gp.RESPONSE_ERROR: serializer.errors
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
 # Lead Detail API [GET<id>, PUT<id>, DELETE<id>]
class LeadDetailViewAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, lead_id):
        try:
            leads = Lead.objects.get(id=lead_id, is_delete=False)
            serializer = LeadSerializer(leads)
            msg = {
            gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
            gp.RESPONSE_KEY : gp.RESPONSE_OK_MSG,
            gp.DATA : serializer.data
            }
            return Response(msg, status=status.HTTP_200_OK)
        except Lead.DoesNotExist:
            msg = {
                gp.RESPONSE_ERROR : gp.LEAD_NOT_FOUND_ERROR
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       

    def put(self, request, lead_id):
        try:
            leads = Lead.objects.get(id=lead_id, is_delete=False)
            serializer = LeadSerializer(leads, data=request.data)
            if serializer.is_valid():
                serializer.save(updated_at=timezone.now(), updated_by=request.user) 
                msg = {
                gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                gp.RESPONSE_KEY : gp.RESPONSE_SUCCESS_MSG,
                gp.DATA : serializer.data
                }
                return Response(msg, status=status.HTTP_201_CREATED)
            msg = {
                gp.RESPONSE_CODE_KEY : gp.UNSUCCESS_CODE,
                gp.RESPONSE_ERROR : serializer.errors
            }
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        except Lead.DoesNotExist:
            msg = {
                gp.RESPONSE_ERROR : gp.LEAD_NOT_FOUND_ERROR
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, lead_id):
        try:
            lead = Lead.objects.get(id=lead_id, is_delete=False)
            lead.is_delete=True
            lead.save()
            msg = {
                gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                gp.RESPONSE_KEY : gp.RESPONSE_SUCCESS_MSG,
            }
            return Response(msg, status=status.HTTP_200_OK)
        except Exception as e:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Company API  [GET, POST]
class CompanyApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            company = Company.objects.filter(is_delete=False)
            serializer = CompanySerializer(company, many=True)
            msg = {
                gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                gp.RESPONSE_KEY : gp.RESPONSE_OK_MSG,
                gp.DATA : serializer.data
            }
            return Response(msg, status=status.HTTP_200_OK)
        except Exception as exe:
            msg ={
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(created_by=request.user, created_at=timezone.now())
                msg = {
                    gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                    gp.RESPONSE_KEY : gp.RESPONSE_SUCCESS_MSG,
                    gp.DATA : serializer.data
                }
                return Response(msg, status=status.HTTP_201_CREATED)
            msg = {
                gp.RESPONSE_CODE_KEY : gp.UNSUCCESS_CODE,
                gp.RESPONSE_ERROR : serializer.errors
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exe:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# class Company detail API [GET<id>, PUT<id>, DELETE<id>]
class CompanyDetailApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id, is_delete=False)
            serializer = CompanySerializer(company)
            msg = {
                gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                gp.RESPONSE_KEY : gp.RESPONSE_OK_MSG,
                gp.DATA : serializer.data
            }
            return Response(msg, status=status.HTTP_200_OK)
        except Company.DoesNotExist:
            msg = {
                gp.RESPONSE_ERROR : gp.COMPANY_NOT_FORUND_ERROR
            }
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        except Exception as exe:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id, is_delete=False)
            serializer = CompanySerializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save(updated_at=timezone.now(), updated_by=request.user)
                msg = {
                    gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                    gp.RESPONSE_KEY : gp.RESPONSE_SUCCESS_MSG,
                    gp.DATA : serializer.data
                }
                return Response(msg, status=status.HTTP_200_OK)
            msg ={
                gp.RESPONSE_CODE_KEY : gp.UNSUCCESS_CODE,
                gp.RESPONSE_ERROR : serializer.error
            }
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
      
    
    def delete(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id, is_delete=False)
            company.is_delete=True
            company.save()
            msg = {
                gp.RESPONSE_CODE_KEY : gp.SUCCESS_CODE,
                gp.RESPONSE_KEY : gp.RESPONSE_SUCCESS_MSG
            }
            return Response(msg, status=status.HTTP_200_OK)
        except Exception as exe:
            msg = {
                gp.RESPONSE_ERROR : gp.INTERNAL_SERVER_ERROR
            }
            return Response(msg, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



