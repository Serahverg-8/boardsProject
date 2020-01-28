from django.shortcuts import render,get_object_or_404
from .models import Board
# Create your views here.
def home_view(request):
    boards = Board.objects.all()
    return render(request, 'boards/home.html', {'boards': boards})

def boardtopics_view(request,board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/topics.html', {'board': board})

#starting a new topic say under id 1 or boards. so again we need the id 

def newtopic_view(request,board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'boards/newtopic.html', {'board': board})