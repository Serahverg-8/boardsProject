from django.shortcuts import render
from .models import Board
# Create your views here.
def home_view(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})