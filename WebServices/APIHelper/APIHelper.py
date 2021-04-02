import requests
import json
from urllib.parse import quote
from requests import get

class APIHelper:

    @staticmethod
    def RenderDashboard(DashboardId, TimeOut , URL):
        URL_T = 'http://localhost:3000/testDashboard'
        FinalPayload = {}
        FinalPayload['dashboardId'] = str(DashboardId)
        FinalPayload['TimeOut'] = str(TimeOut)
        FinalPayload['URL'] = URL
        Response = requests.post(url=URL_T, json=FinalPayload).json()
        return Response





