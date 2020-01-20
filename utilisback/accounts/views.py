from django.shortcuts import render
from .models import Members
from .serializers import MemberSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class MemberView(APIView):

    def get(self, request, format=None):
        snippets = Members.objects.all()
        serializer = MemberSerializer(snippets, many=True)
        data_dict = {"status":200, "data":serializer.data}
        return Response(data_dict, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data_dict = {"status":201, "data":serializer.data}
            return Response(data_dict, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors, "status":400}, status=status.HTTP_400_BAD_REQUEST)
