from django.urls import path
from .views import FizzBuzzView

urlpatterns = [
    path('', FizzBuzzView.as_view(), name='fizz-buzz'),
    path('<int:since>-<int:until>/', FizzBuzzView.as_view(), name='fizz-buzz-params'),
]
