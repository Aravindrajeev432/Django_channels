from django.urls import path
from .views import First,MakeBusy,MakeFree
urlpatterns = [
    path('chat',First.as_view(),name="first"),
   path('busy/<int:id>',MakeBusy.as_view(),name="free"),
   path('free/<int:id>',MakeFree.as_view())

]