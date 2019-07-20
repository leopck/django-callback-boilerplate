from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
import json

import requests

from .models import Distribution

#  curl -X POST -H "Content-Type: application/json" -d "2.1" -u admin:build@123 http://192.168.0.101:9090/idealweight/
#  curl -X POST -H "Content-Type: application/json" -d '{"version": "30070","rpm": "AVB-AudioModules-4.1.0-1.x86_64.rpm"}' -u admin:build@123 http://puer-tea.png.intel.com:9090/idealweight/
#  curl -X POST -H "Content-Type: application/json" -d '{"version": "29460","rpm": "Babel-2.6.0-66.x86_64.rpm"}' -u admin:build@123 http://puer-tea.png.intel.com:9090/idealweight/

class DistributionView(APIView):
    """
    This sample was created using this: https://stackoverflow.com/questions/33315436/django-rest-framework-router-how-to-add-customized-url-and-view-functions/33320234#33320234
    """

    def get(self, request):
        """POST - Add new distribution"""
        dist = Distribution.objects.all()
        return Response({"distribution": dist})
        



# @api_view(["POST"])
# def IdealWeight(post_data_json):
#     print(str(post_data_json.data))
#     json_output = 0
#     version_array = []

#     try:
#         json_output=json.loads(str(post_data_json.data).replace("\'", '\"'))
#         tmpVersion = json_output['version'].replace(' ', '')
#         nocomma = tmpVersion.split(',')

#         if len(nocomma) != 1:
#             for target_list in nocomma:
#                 pass
#             version_array.append()

#         # multiple output:
#         # version: 20000
#         # version: 20000, 30000
#         # version: 20000 - 30000
#         # version: 20000-30000
#         # version: 20000,30000-40000
#         # version: 20000 - 30000, 40000
#         # version: 20000, 30000, 40000
#         # version: 20000 - 30000 - 40000 #invalid must error out


#         print(json_output['version'])
#         print(json_output['rpm'])
#         URL = 'http://linux-ftp.jf.intel.com/pub/mirrors/clearlinux/releases/' + str(json_output['version']) + '/clear/x86_64/os/Packages/' + json_output['rpm']
#         header = {
#             'Authorization': 'Bearer AAAENIDzikPUX8q3jQdy7FyBZze1Gp/Km6wKolWCilocjxY4',
#             'Group': '36',
#             'Url': URL,
#         }
#         res = requests.post('https://protecode.devtools.intel.com/api/fetch/', headers=header, verify=False)
#         return JsonResponse(str(res.content),safe=False)
#     except ValueError as e:
#         return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
# def Rebecca(post_data_json):
#     print("hELLO " + str(post_data_json.data))
#     return Response("hELLO " + str(post_data_json.data))