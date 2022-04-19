from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ArchitectureViewSet, CreateUserViewSet, GetAllProjectsByArchiProfileView, GetAllProjectsListView, GetProjectDetailsView, PostProjectViewset, UserViewSet ,ClientAccountViewSet, getUserDetails, showHomePageListView
from rest_framework.authtoken.views import obtain_auth_token

routes = DefaultRouter()
# routes.register('userslist',UserViewSet.as_view(),basename="all_users")
# routes.register('create/user',CreateUserViewSet,basename="create_user")
routes.register('getclients',ClientAccountViewSet,basename="all_client")
routes.register('getarchi',ArchitectureViewSet,basename="all_architectures_list")
routes.register('postproject',PostProjectViewset,basename="Post_projects")   # set user by header
# routes.register('home',homeScreen,basename="home_page")


urlpatterns = [
    path('',include(routes.urls)),
    path('auth/login/',obtain_auth_token,name="create-token"),  #Login Api
    path('create/user/',CreateUserViewSet.as_view(),name="create_user"),  #Sign up
    path('userslist/',UserViewSet.as_view(),name="all_users"),  # get All user
    path('user/account/',getUserDetails.as_view(),name="get_user_details"), #Get account of loggedin user
    path('get/home/',showHomePageListView.as_view(),name="Fetch_list"), # Fetch list according 
    path('getproject/',GetAllProjectsListView.as_view(),name="Get_projects"), # Fetch list according 
    path('getArchiproject/',GetAllProjectsByArchiProfileView.as_view(),name="Get_archi_projects"), # Fetch list according 
    path('getproject/<int:pk>/',GetProjectDetailsView.as_view(),name="Get_projects"), # Fetch list according 
]
