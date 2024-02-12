from rest_framework.response import Response
from rest_framework.views import APIView
from data_uploader.models import CompanyData
from django.shortcuts import render
from django.db.models import Q
class CountData(APIView):
    def get(self, request):
        req_params = request.query_params

        req_params = request.query_params
        if any(req_params.values()):
            filters = Q()
            if req_params.get('keyword'):
                filters |= Q(name__icontains=req_params['keyword'].lower())
            if req_params.get('yearFounded'):
                filters |= Q(year_founded=req_params['yearFounded'])
            if req_params.get('city'):
                filters |= Q(city=req_params['city'])
            if req_params.get('state'):
                filters |= Q(state=req_params['state'])
            if req_params.get('country'):
                filters |= Q(country=req_params['country'])
            if req_params.get('employeesFrom'):
                filters |= Q()
            if filters:
                count = CompanyData.objects.filter(filters).count()
            else:
                count = CompanyData.objects.all().count()
        else:
            count = CompanyData.objects.all().count()
        
        return Response({'count': count})

def index(request):
    industries = CompanyData.objects.values_list('industry', flat=True).distinct()
    year_founded = CompanyData.objects.values_list('year_founded', flat=True).distinct()
    cities = CompanyData.objects.values_list('city', flat=True).distinct()
    states = CompanyData.objects.values_list('state', flat=True).distinct()
    countries = CompanyData.objects.values_list('country', flat=True).distinct()

    return render(request, 'query_builder/index.html', {'industries': industries, 'year_founded': year_founded, 'cities': cities, 'states': states, 'countries': countries})