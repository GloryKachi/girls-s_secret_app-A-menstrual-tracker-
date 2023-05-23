from django.urls import path
from .views import details

urlpatterns = [
    # path('', homepage, name='home'),
    path('', details, name='detail')

]
