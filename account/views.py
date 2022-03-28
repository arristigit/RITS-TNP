from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

from account.serializer import StudentSerializer, FacultySerializer
from account.models import Student, Faculty


class StudentView(APIView):
    serializer_class = StudentSerializer

    def get(self, request, pk=None, format=None):
        if pk is not None:
            obj = Student.objects.get(id=pk)
            serializer = StudentSerializer(obj)
            return Response(serializer.data)

        obj = Student.objects.all()
        serializer = StudentSerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success! The Student has been created."}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        obj = Student.objects.get(id=pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Success! The Student has been updated completly."}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None, format=None):
        obj = Student.objects.get(id=pk)
        serialzer = StudentSerializer(obj, data=request.data, partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"message":"Success! The Student has been updated paritially."}, status=status.HTTP_202_ACCEPTED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        obj = Student.objects.get(id=pk)
        obj.delete()
        return Response({"message":"Success! The Student has been deleted."})


class FacultyView(APIView):
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is not None:
            obj = Faculty.objects.get(id=pk)
            serializer = FacultySerializer(obj)
            return Response(serializer.data)

        obj = Faculty.objects.all()
        serializer = FacultySerializer(obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success! The Faculty has been created."}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        obj = Faculty.objects.get(id=pk)
        serializer = FacultySerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Success! The Faculty has been updated completly."}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None, format=None):
        obj = Faculty.objects.get(id=pk)
        serialzer = FacultySerializer(obj, data=request.data, partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response({"message":"Success! The Faculty has been updated paritially."}, status=status.HTTP_202_ACCEPTED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        obj = Faculty.objects.get(id=pk)
        obj.delete()
        return Response({"message":"Success! The Faculty has been deleted."})