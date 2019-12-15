from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from . import video_openpose


class SampleEndPoint(APIView):

    def post(self, request):
        if request.data:
            print(request.data)
            # data = json.loads(request.data)
            # print(data)
            return Response({"message": "Successfully received"})

        else:
            return Response({"message": "Aditya is a Chutiya"})


class SampleRun(APIView):

    def get(self, request):
        l = video_openpose.adjust_video_fps('/data/vid_edit.mp4')
        print(l)
        return Response({"status": 'success'})
