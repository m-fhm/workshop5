from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import usermodel
from . forms import userforms
# Create your views here.

from .serializers import userserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def get(request):
    fetch = usermodel.objects.all()
    serializer = userserializer(fetch, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def post(request):
    data = {
        'name' : request.data.get('name'),
        'last' : request.data.get('last'),
        'email' : request.data.get('email')
      }

    serializer = userserializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
    



def index(request):
    db_data = usermodel.objects.all()
    if request.GET:
        form_data =userforms(request.GET)
        if form_data.is_valid():
            form_data.save()

        # data = request.GET.dict()
        # name = data['name']
        # last = data['last']
        # email = data['email']
        # form_data = usermodel(name=name,last=last,email=email)
        # form_data.save()

    form = userforms()
    return render(request,'index.html',{'db':db_data, 'form':form})


def update(request,id):
    fetch=usermodel.objects.get(id=id)
    
    form = userforms(request.POST or None, instance=fetch)
    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'update.html',{'fm':form})

def delete(request,id):
    fetch=usermodel.objects.get(id=id)
    fetch.delete()
    return redirect('index')


