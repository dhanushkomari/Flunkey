from django.shortcuts import render, redirect
from .models import Bot, Table, Delivery,FinalDelivery
from .forms import Deliveryform
from django.http import HttpResponse
from time import time

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BotSerializer, FinalDeliverySerializer, TableSerializer

# Create your views here.

def DisplayBots(request):
    b = Bot.objects.filter(avialable = True)
    bn = Bot.objects.filter(avialable = False)
    
    return render(request, 'api/home.html', {'b':b, 'bn':bn})



def DisplayTables(request):

    t = Table.objects.filter(avialable = True)
    tn = Table.objects.filter(avialable = False)
    print(tn)

    return render(request, 'api/display-table.html', {'t':t, 'tn':tn})



def DisplayOptions(request):
    d = Delivery.objects.latest('pk')
    if request.method == "POST":
        d.speed_of_the_bot = request.POST['speed_of_the_bot']
        d.food_type = request.POST['food_type']
        d.save()

        FD = FinalDelivery.objects.create(
                                          bot_no = d.bot_no,
                                          bot_name = d.bot_name,
                                          table_no = d.table_no,
                                          ip = d.ip,
                                          port = d.port,
                                          food_type = d.food_type,
                                          speed_of_the_bot = d.speed_of_the_bot,
                                          time = time()
                                        )

        print(d.speed_of_the_bot, d.food_type)
        return redirect('api:display-op')

    form = Deliveryform()
    return render(request, 'api/options.html', {'form':form})

def DisplayOP(request):
    d = FinalDelivery.objects.latest('pk')
    return render(request, 'api/op.html', {'d':d})



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

    

def selectTable(request,id):
    t = Table.objects.get(id = id)
    print(t.table_number)
    d = Delivery.objects.latest('pk')
    d.table_no = t.table_number
    d.save()
    return redirect('api:select-options')

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
