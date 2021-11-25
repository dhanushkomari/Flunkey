from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.Login, name = 'login'),
    path('logout/', views.Logout, name = 'logout'),
    path('bots', views.DisplayBots, name = 'bots'),
    path('tables', views.DisplayTables, name = 'table'),
    path('options/', views.DisplayOptions, name  = 'select-options'),
    path('bot/<str:id>', views.selectBot, name = 'select-bot'),
    path('table/<str:id>', views.selectTable, name = 'select-table'),

    path('all', views.Alldeliveries, name = 'all-deliveries'),
    path('latest', views.latestDelivery, name = 'latest-delivery'),

    path('update-bot/<str:bot_no>', views.updateBot, name = 'update-bot'),
    path('update-battery/<str:bot_no>', views.updateBattery, name = 'update-battery'),

    path('success/', views.DisplayOP, name = 'display-op'),
    path('end-today', views.DeleteTimeInDeliView, name = 'end-today'),
    path('update-table/<str:table_no>', views.updateTable, name = 'update-table')
]
