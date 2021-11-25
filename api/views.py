from django.shortcuts import render, redirect
from .models import Bot, Table, Delivery,FinalDelivery
from .forms import Deliveryform
from django.http import HttpResponse
from time import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BotSerializer, FinalDeliverySerializer, TableSerializer, BatterySerializer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('api:bots')            
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('api:login')
    else:
        return render(request, 'api/login.html')

@login_required
def Logout(request):
    logout(request)
    messages.info(request, "logged out successfully")
    return redirect('api:login')

@login_required
def DisplayBots(request):
    b = Bot.objects.filter(avialable = True)
    bn = Bot.objects.filter(avialable = False)
    
    return render(request, 'api/home.html', {'b':b, 'bn':bn})


@login_required
def DisplayTables(request):

    t = Table.objects.filter(avialable = True)
    tn = Table.objects.filter(avialable = False)
    print(tn)

    return render(request, 'api/display-table.html', {'t':t, 'tn':tn})


@login_required
def DisplayOptions(request):
    d = Delivery.objects.latest('pk')
    if request.method == "POST":
        # d.speed_of_the_bot = request.POST['speed_of_the_bot']
        # d.food_type = request.POST['food_type']
        # d.save()

        FD = FinalDelivery.objects.create(
                                          bot_no = d.bot_no,
                                          bot_name = d.bot_name,
                                          table_no = d.table_no,
                                          ip = d.ip,
                                          port = d.port,
                                        #   food_type = d.food_type,
                                        #   speed_of_the_bot = d.speed_of_the_bot,
                                          time = time()
                                        )

        # print(d.speed_of_the_bot, d.food_type)
        return redirect('api:display-op')

    
    return render(request, 'api/options.html', {'d':d})

def DisplayOP(request):
    d = FinalDelivery.objects.latest('pk')
    return render(request, 'api/op.html', {'d':d})


@login_required
def selectBot(request, id):
    b = Bot.objects.get(id = id)
    d = Delivery.objects.create(
                                 bot_no =  b.bot_no,
                                 bot_name = b.name,
                                 ip = b.ip,
                                 port = b.port,  
                                )   
    d.save()
    return redirect('api:table')

    
@login_required
def selectTable(request,id):
    t = Table.objects.get(id = id)
    print(t.table_number)
    d = Delivery.objects.latest('pk')
    d.table_no = t.table_number
    d.save()
    return redirect('api:select-options')

    

@login_required
def DeleteTimeInDeliView(request):
    obj = FinalDelivery.objects.latest('pk')
    obj.time = 0
    obj.save()

    return redirect('api:bots')


####################################################################################################
#########################################    REST API VIEWS   ######################################
####################################################################################################

@api_view(['GET'])
def Alldeliveries(request):
    d = FinalDelivery.objects.all()
    serializer = FinalDeliverySerializer(d, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def latestDelivery(request):
    d = FinalDelivery.objects.latest('pk')
    serializer = FinalDeliverySerializer(d, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def updateBot(request, bot_no):
    b = Bot.objects.get(bot_no = bot_no)
    serializer = BotSerializer(instance = b, data = request.POST)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateTable(request, table_no):
    t = Table.objects.get(table_number = table_no)
    serializer = TableSerializer(instance =t, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateBattery(request, bot_no):
    b = Bot.objects.get(bot_no = bot_no)
    serializer = BatterySerializer(instance = b, data = request.POST)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
