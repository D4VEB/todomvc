from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from todo.serializers import TodoSerializer
from todo.models import Todo


# class ListCreateTodo(APIView):
#
#     def get(self, request, pk):
#         try:
#             todo = Todo.objects.get(pk=pk)
#         except Todo.DoesNotExist as e:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#         serializer = TodoSerializer(todo, context={'request':request})
#         return Response(serializer.data)

@api_view(['GET', 'POST'])
def list_create_todo(request):
    if request.method == 'GET':
        todo = Todo.objects.order_by('-created_at')
        serializer=TodoSerializer(todo, many=True, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailUpdateDeleteTodo(APIView):

    def get_todo(pk):
        try:
            todo = Todo.objects.get(pk=pk)
            return todo
        except Todo.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
    # leaving 'request' here because it's in the example, but I don't think it's necessary
        try:
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        todo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
