from django.shortcuts import render
from django.http import HttpResponse
from . models import usermodel
from . forms import userforms
# Create your views here.


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




