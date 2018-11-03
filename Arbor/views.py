from django.shortcuts import render
from django.template.response import TemplateResponse
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.
def landing(request):
    return TemplateResponse(request, 'arbor_dashboard.html' )



# class Gauge(APIView):
#     authentication_classes = []
#     permission_classes = []
#  
#     def get(self, request, format=None):
#         try:
#             response = requests.get('https://auto-ch2-01p.sys.comcast.net/api/arbor/stat', verify= False)
#             summary = response.json()
#             a_data = {
#                 'value':summary['data']['alert'],
#                 'avg': summary['data']['alert_avg'],
#                 'min': summary['data']['alert_min'],
#                 'max': summary['data']['alert_max']
#                 }
#             
#             m_data = {
#                 'value':summary['data']['mitigation'],
#                 'avg': summary['data']['mit_avg'],
#                 'min': summary['data']['mit_min'],
#                 'max': summary['data']['mit_max']
#                 }
#             return Response(summary)
#         except Exception, e:
#             return [e]

def DeviceData(request):
    try:
        response = requests.get('https://auto-ch2-01p.sys.comcast.net/api/em7/tmsdevices', verify= False)
        summary = response.json()
        devices = summary['tms_devices']
        
#         a_data = {
#             'value':summary['data']['alert'],
#             'avg': summary['data']['alert_avg'],
#             'min': summary['data']['alert_min'],
#             'max': summary['data']['alert_max']
#             }
#          
#         m_data = {
#             'value':summary['data']['mitigation'],
#             'avg': summary['data']['mit_avg'],
#             'min': summary['data']['mit_min'],
#             'max': summary['data']['mit_max']
#             }
#         data = [a_data,m_data]
        
        return JsonResponse({'devices': devices}, safe=False)
    except Exception, e:
        return [e]


def DeviceStat(request):
    try:
        response = requests.get('https://auto-ch2-01p.sys.comcast.net/api/em7/tmsdevices', verify= False)
        summary = response.json()
        devices = summary['tms_devices']
        
#         a_data = {
#             'value':summary['data']['alert'],
#             'avg': summary['data']['alert_avg'],
#             'min': summary['data']['alert_min'],
#             'max': summary['data']['alert_max']
#             }
#          
#         m_data = {
#             'value':summary['data']['mitigation'],
#             'avg': summary['data']['mit_avg'],
#             'min': summary['data']['mit_min'],
#             'max': summary['data']['mit_max']
#             }
#         data = [a_data,m_data]
        
        return render(request, 'arbor_new.html',{'devices': devices})
    except Exception, e:
        return [e]

def ArborData(request):
    try:
        response = requests.get('https://auto-ch2-01p.sys.comcast.net/api/arbor/stat', verify= False)
        summary = response.json()
        
        a_data = {
            'value':summary['data']['alert'],
            'avg': summary['data']['alert_avg'],
            'min': summary['data']['alert_min'],
            'max': summary['data']['alert_max']
            }
         
        m_data = {
            'value':summary['data']['mitigation'],
            'avg': summary['data']['mit_avg'],
            'min': summary['data']['mit_min'],
            'max': summary['data']['mit_max']
            }
#         data = [a_data,m_data]
        return JsonResponse({'alert': a_data, 'mit': m_data}, safe=False)
    except Exception, e:
        return [e]


def getarbor(request):
    try:
        apilist = [1,2,3]
        response = requests.get('https://auto-ch2-01p.sys.comcast.net/api/em7/tmsdevices', verify= False)
        summary = response.json()
        devices = summary['tms_devices']
       
        return render(request, 'arbor_new.html',{'devices': devices})
    except Exception, e:
        return [e]
