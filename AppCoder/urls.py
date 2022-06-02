from django.urls import path
from AppCoder.views import profesores, curso 

urlpatterns = [
    path('curso/', curso),
    path('profesores/', profesores),

]
