from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from mobile.models import mobiles
# Create your views here.

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'mobiles':mobiles})
    def post(self,request,*args,**kwargs):
        print(request.data)
        qs=request.data
        mobiles.append(qs)
        return Response({'msg':request.data})


class MobileDetailsView(APIView):
    def get(self,request,*args,**kwargs):
        print("kwargs",kwargs)
        id=kwargs.get('mob_id')
        details=[mob for mob in mobiles if mob.get('id')==id].pop()
        return Response({'data':details})

