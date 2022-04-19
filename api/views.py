from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .helper import CustomSearchFilter
from .models import ArchitectureAccount, ClientAccount, Project
from .serializers import ArchitectureAccountSerializer, ClientAccountSerializer, ProjectSerializer, UserSerializers
from rest_framework import generics , filters
from rest_framework.response import Response
from rest_framework.authentication import  TokenAuthentication , BasicAuthentication
from rest_framework.permissions import IsAuthenticated , BasePermission
from rest_framework import status

User = get_user_model()
# Create your views here.
class checkPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'POST' or request.method == 'GET'  or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_authenticated :
                return True
        return False


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class CreateUserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     serializer.save(user = self.request.user)

class ClientAccountViewSet(ModelViewSet):
    queryset = ClientAccount.objects.all()
    serializer_class = ClientAccountSerializer
    permission_classes = [checkPermission, IsAuthenticated ]
    authentication_classes = [BasicAuthentication ,TokenAuthentication ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['Username','Name','city']


    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user = self.request.user)

class ArchitectureViewSet(ModelViewSet):
    queryset = ArchitectureAccount.objects.all()
    serializer_class = ArchitectureAccountSerializer
    permission_classes = [checkPermission, IsAuthenticated ]
    authentication_classes = [BasicAuthentication ,TokenAuthentication ]
    filter_backends = [filters.SearchFilter]
    search_fields = ['Username','Name','city']


class getUserDetails(generics.ListAPIView,generics.RetrieveAPIView):
    # queryset = ClientAccount.objects.all()
    # serializer_class = ClientAccountSerializer
    permission_classes = [checkPermission, IsAuthenticated ]
    authentication_classes = [ TokenAuthentication ]

    def get_queryset(self):
        print(self.request.user.user_role)
        if self.request.user.user_role == "A":
            user_id = self.request.user
            return ArchitectureAccount.objects.filter(user = user_id)
            # return ArchitectureAccount.objects.all()
        else:
            user_id = self.request.user
            return ClientAccount.objects.filter(user = user_id)
            # return ClientAccount.objects.all()

    def list(self, request, *args, **kwargs):
        # print(super())
        # return Response({"data":'hey'})
        return super().list(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.user.user_role == "A":
            return ArchitectureAccountSerializer
        else:
            return ClientAccountSerializer

    # def get_queryset(self):
    #     user_id = self.request.user
    #     return ClientAccount.objects.filter(user = user_id)


class showHomePageListView(generics.ListAPIView):
    # queryset = ClientAccount.objects.all()
    # serializer_class = ClientAccountSerializer
    permission_classes = [checkPermission, IsAuthenticated ]
    authentication_classes = [BasicAuthentication, TokenAuthentication ]
    filter_backends = [filters.SearchFilter]
    # if request.user.user_role == "C":
    filter_class= CustomSearchFilter
    search_fields = ['Username','Name','city']


    # def __init__(self,request) -> None:
    #     print('hey',request)
    #     # self.search_fields = 
    #     super().__init__(**kwargs)

    # def get_search_fields(self, view, request):
    #     if self.request.user.user_role == "C":
    #         print('C')
    #         return ['Username','Name','city']
    #     elif self.request.user.user_role == "A":
    #         print('a')

    #         return ['name','desc']
    #     return ['name','desc']
        # return super().get_search_fields(view, request)



    def get_queryset(self):
        if self.request.user.user_role == "C":
            return ArchitectureAccount.objects.all()

        else:
            return Project.objects.all()
            # return ClientAccount.objects.all()




    def get_serializer_class(self):
        if self.request.user.user_role == "C":
            return ArchitectureAccountSerializer
        else:
            return ProjectSerializer


class PostProjectViewset(ModelViewSet):
    '''
        GET :- Fetching project of user have posted
    '''
    # class PostProjectViewset(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [checkPermission, IsAuthenticated ]
    authentication_classes = [ BasicAuthentication,TokenAuthentication ]
    
    def perform_create(self, serializer):
        print(self.request.user)
        ins= ClientAccount.objects.get(user=self.request.user.id)
        # print(ins)
        serializer.save(posted_by = ins)


    def get_queryset(self):
        # print(self.request.user.user_role)
        user_id = self.request.user.id
        print(user_id,"method: ==>",self.request.method)
        return Project.objects.filter(posted_by = user_id)
        # return Project.objects.all()

    # def retrieve(self, request, *args, **kwargs):

    #     return super().retrieve(request, *args, **kwargs)

    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

class GetAllProjectsListView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [checkPermission, IsAuthenticated ]
    authentication_classes = [ BasicAuthentication,TokenAuthentication ]

class GetProjectDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class GetAllProjectsByArchiProfileView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        id = self.request.user.id
        print(self.request.user,id)
        print(Project.objects.filter(apply_for=id))
        return super().get_queryset()
    
    