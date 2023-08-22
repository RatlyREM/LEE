from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from Exer.models import Exercise
from routine.models import Routine
from usebody.models import Usebody
from routine.serializers import RoutineSerializer
from django.shortcuts import get_object_or_404

#루틴 생성
class RoutineCreateAPIView(APIView):
    def post(self,request):
        #전달되는 값들?
        routine_data = { #이 값들은 반드시 전달되어야 함(owner_id도?)
             'routine_name' : request.data.get('routine_name'),
             'routine_comment' : request.data.get('routine_comment'),
             'routine_day' : request.data.get('routine_day'),
             'owner_id' : request.data.get('owner_id'),
        } #없는 부분들을 default 설정만 하면 되는가? 아니면 여기서 따로 설정해줘야 하는가?
        #이런 식으로 부분만 전달하면, is_valid의 유효성 검사에 안 걸리나?
        #우선 지피티에선 default값을 설정해두면 안 걸린다고 보긴 함.
        #빈 데이터가 전달되는거랑 아예 request data에 항목이 없는 거랑 좀 다르지 않나?

        #serializer = RoutineSerializer(data=request.data)
        serializer = RoutineSerializer(data=routine_data)

        if serializer.is_valid():
            instance = serializer.save()
            # return Response(serializer.data, status=201)
            return Response(instance, status=201)
        return Response(serializer.errors, status=400)

#루틴 조회
class RoutineCheckAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Routine, pk=pk)

    def get(self, request,pk):
        routine = self.get_object(pk)
        serializer = RoutineSerializer(routine)
        return Response(serializer.data)

#루틴 수정
class RoutinePutAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Routine, pk=pk)

    def put(self,request, pk):
        routine = self.get_object(pk)
        serializer = RoutineSerializer(routine, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


#루틴 삭제
class RoutineDeleteAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Routine, pk=pk)

    def delete(self, request, pk):
        routine = self.get_object(pk)
        routine.delete()

        return Response(status=204)


#루틴 세부사항 생성

#class RoutineDetailCreateAPIView(APIView):
    #전달되는 값들
    # routineDetail_data = {
    #     routine_id: pk,
    #     exercise: request.data.get('exercise_id'),
    #     usebody: request.data.get('usebody_id'),
    #     day: request.data.get('day'),
    # }

    #serializer = RoutineDetailSerializer(data=routineDetail_data)



