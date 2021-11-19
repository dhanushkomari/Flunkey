from django.shortcuts import render
from api.models import Bot, FinalDelivery, Table
from dashboard.models import Bot_location, Map

from .serializers import LocationSerializer, MapSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import date, datetime

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

def dashbaord(request): 
    # all food deliveries
    fd = FinalDelivery.objects.filter(food_delivered = True)

    # todays deliveries
    td = FinalDelivery.objects.filter(created_at__date = date.today(), food_delivered = True) 

    # active bots 
    ab = Bot.objects.filter(status = True)

    # avialable tables
    at = Table.objects.filter(avialable = True)

    return render(request, 'dashboard/dashboard.html', {
                                                        'fd': len(fd), 
                                                        'td': len(td), 
                                                        'ab': len(ab),
                                                        'at': len(at),
                                                        'abl': ab,
                                                        }
                )

    
def bot_dashboard(request, bot_name):
    if request.method == "POST":
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        fd = FinalDelivery.objects.filter(created_at__range=(startdate, enddate))

        return render(request, 'dashboard/bot_dashboard.html')

    else:
        bot = Bot.objects.get(name = bot_name)
        bot_name = bot.name
        bot_loc = Bot_location.objects.get(bot__name = bot_name)

        fd = FinalDelivery.objects.filter(food_delivered = True, bot_name = bot_name)

        td = FinalDelivery.objects.filter(created_at__date = date.today(), food_delivered = True, bot_name = bot_name) 


        date1 = datetime.today()
        week = date1.strftime('%V')
        print(week)
        tw = FinalDelivery.objects.filter(created_at__week = week, food_delivered = True, bot_name = bot_name)

        return render(request, 'dashboard/bot_dashboard.html', {
                                                                'fd':len(fd),
                                                                'td':len(td),
                                                                'bot_name':bot_name, 
                                                                'bot':bot,  
                                                                'bot_loc':bot_loc,
                                                                'tw':len(tw),
                                                                })
@api_view(['POST'])
def updateLocation(request, bot_name):
    bot = Bot.objects.get(name = bot_name)
    bot_loc = Bot_location.objects.get(bot__name = bot.name)
    print(bot)
    serializer = LocationSerializer(instance = bot_loc, data = request.POST)
    if serializer.is_valid():
        serializer.save()
        print(serializer.data)
    return Response(serializer.data)


def mapView(request):
    m = Map.objects.latest('pk')
    return render(request, 'dashboard/map_dashboard.html', {'m': m})

class updateMap(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        m = Map.objects.latest('pk')
        
        file_serializer = MapSerializer(instance = m, data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
