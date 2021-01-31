from django.shortcuts import render
from .models import Verb, Numeral
from .serializers import VerbSerializer, NumeralSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter, FilterSet
from django.contrib.auth.models import User
from rest_framework import generics

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'

class NumeralFilter(NumberFilter):
    from_cardinal = NumberFilter(field_name='cardinal', lookup_expr='gte')
    to_cardinal = NumberFilter(field_name='cardinal', lookup_expr='lte')
    class Meta:
        model = Numeral
        fields =['from_cardinal','to_cardinal']

class VerbList(generics.ListCreateAPIView):
    queryset = Verb.objects.all()
    serializer_class = VerbSerializer
    name = 'verb-list'
    filter_fields = ['infinitive','past_tense','past_participle','translation']
    search_fields = ['infinitive','past_tense','past_participle','translation']
    ordering_fields = ['infinitive','past_tense','past_participle','translation']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class NumeralList(generics.ListCreateAPIView):
    queryset = Numeral.objects.all()
    serializer_class = NumeralSerializer
    filter_class = NumeralFilter
    name = 'numeral-list'
    filter_fields = ['cardinal_number', 'ordinal_number', 'translation']
    search_fields = ['cardinal_number', 'ordinal_number', 'translation']
    ordering_fields = ['cardinal_number', 'ordinal_number', 'translation']


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'verb': reverse(VerbList.name, request=request),
                         'numeral': reverse(NumeralList.name, request=request),
                         'users': reverse(UserList.name, request=request)
                          })

'''@api_view(['GET','POST'])
def question_list(request, format=None):
    if request.method == 'GET':
        questions = Question.objects.all()
        seralizer  = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def question_detail(request, pk, format=None):
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
            return Response(serializer.data)

    if request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return HttpResponse(status=status.HTTP_204)_NO_CONTENT)
'''