from django.urls import path,include
from employee import views



urlpatterns=[

    path('', views.emp,name='emp'),

    path('holiday/', views.holiday,name='holiday')
]