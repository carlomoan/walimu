from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model

#User = get_user_model()
# Create your views here.
class UserView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated] # checks if user is authenticated to view the model objects

    def get_queryset(self):
        return User.objects.all() #returns all models objects.

    def get(self, request, *args, **kwargs): # GET request handler for the model
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = UserSerializer

    def dispatch(self, request, *args, **kwargs):
        if kwargs.get('pk') == 'current' and request.user:
            kwargs['pk'] = request.user.pk

        return super(UserViewSet, self).dispatch(request, *args, **kwargs)

class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]    

class UsersProfileView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ListMitaalaView(generics.ListAPIView):
    queryset = Mitaala.objects.all()
    serializer_class = MitaalaSerializer
    permission_classes = [IsAuthenticated]

class mtaalalist(generics.ListAPIView):
    queryset = Mitaala.objects.all()
    serializer_class = MitaalaSerializer
    permission_classes = [AllowAny]

    ''' def select_mtaala(self,request,pk = none):
        if 'mtaala_id' in request.data:
            title=title.object '''


class MitaalaDetail(generics.RetrieveAPIView):
    queryset = Mitaala.objects.all()
    serializer_class = MitaalaSerializer
    permission_classes = [IsAuthenticated]

class ListDarasaView(generics.ListAPIView):
    queryset = Darasa.objects.all()
    serializer_class = DarasaSerializer
    permission_classes = [IsAuthenticated]

class DarasaDetail(generics.RetrieveAPIView):
    queryset = Darasa.objects.all()
    serializer_class = DarasaSerializer
    permission_classes = [IsAuthenticated]

class ListUmahiriView(generics.ListAPIView):
    queryset = Umahiri.objects.all()
    serializer_class = UmahiriSerializer
    permission_classes = [IsAuthenticated]

class UmahiriDetail(generics.RetrieveAPIView):
    queryset = Umahiri.objects.all()
    serializer_class = UmahiriSerializer
    permission_classes = [IsAuthenticated]

class ListUmahsusiView(generics.ListAPIView):
    queryset = Umahsusi.objects.all()
    serializer_class = UmahsusiSerializer
    permission_classes = [IsAuthenticated]

class UmahsusiDetail(generics.RetrieveAPIView):
    queryset = Umahsusi.objects.all()
    serializer_class = UmahsusiSerializer
    permission_classes = [IsAuthenticated]

class ListMuhulaView(generics.ListAPIView):
    queryset = Muhula.objects.all()
    serializer_class = MuhulaSerializer
    permission_classes = [IsAuthenticated]

class MuhulaDetail(generics.RetrieveAPIView):
    queryset = Umahsusi.objects.all()
    serializer_class = MuhulaSerializer
    permission_classes = [IsAuthenticated]

class ListJumaView(generics.ListAPIView):
    queryset = Juma.objects.all()
    serializer_class = JumaSerializer
    permission_classes = [IsAuthenticated]

class JumaDetail(generics.RetrieveAPIView):
    queryset = Juma.objects.all()
    serializer_class = JumaSerializer
    permission_classes = [IsAuthenticated]

class ListSikuView(generics.ListAPIView):
    queryset = Siku.objects.all()
    serializer_class = SikuSerializer
    permission_classes = [IsAuthenticated]

class SikuDetail(generics.RetrieveAPIView):
    queryset = Siku.objects.all()
    serializer_class = SikuSerializer
    permission_classes = [IsAuthenticated]

class ListShughuliView(generics.ListAPIView):
    queryset = Shughuli.objects.all()
    serializer_class = ShughuliSerializer
    permission_classes = [IsAuthenticated]

class ShughuliDetail(generics.RetrieveAPIView):
    queryset = Shughuli.objects.all()
    serializer_class = ShughuliSerializer
    permission_classes = [IsAuthenticated]

class ListVipindiView(generics.ListAPIView):
    queryset = Vipindi.objects.all()
    serializer_class = VipindiSerializer
    permission_classes = [IsAuthenticated]

class VipindiDetail(generics.RetrieveAPIView):
    queryset = Vipindi.objects.all()
    serializer_class = VipindiSerializer
    permission_classes = [IsAuthenticated]

class ListMtaalaHead(generics.ListAPIView):
    queryset = MtaalaHead.objects.all()
    serializer_class = MtaalaHeadSerializer
    permission_classes = [IsAuthenticated]

class MtaalaHeadDetail(generics.RetrieveAPIView):
    queryset = MtaalaHead.objects.all()
    serializer_class = MtaalaHeadSerializer
    permission_classes = [IsAuthenticated]

class ListMtaalaArticle(generics.ListAPIView):
    queryset = MtaalaArticles.objects.all()
    serializer_class = MtaalaArticleSerializer
    permission_classes = [IsAuthenticated]

class MtaalaArticlesDetail(generics.RetrieveAPIView):
    queryset = MtaalaArticles.objects.all()
    serializer_class = MtaalaArticleSerializer
    permission_classes = [IsAuthenticated]

@api_view(['POST'])
def RegisterView(request):
    if request.method =='POST':
        serializer=RegistrationSerializer(data=request.data)
        permission_classes = [AllowAny]
        data={}
        if serializer.is_valid():
            user=serializer.save()
            data['response']= "Successfully registered a new user"
            data['email']=user.email
            data['username']=user.username
        else:
            data=serializer.errors
        return Response(data)


def index(request):
    return render(request, 'index.html')

class HomeView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return Darasa.objects.all()

def darasadetail(request, id):
    darasa = Darasa.objects.get(id=id)
    return render(request, 'darasa.html', {'darasa': darasa})

class MtaalaList(ListView):
    model = Mitaala

def mtaaladetail(request, id):
    curricula = Mitaala.objects.get(id=id)
    return render(request, 'curricula_list.html', {'mitaala': mitaala})

class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)