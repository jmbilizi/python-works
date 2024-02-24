from django.http import HttpResponse
from django.shortcuts import render

# Create your views here (Request handler).

def say_hello(request):
    return HttpResponse('Hello World!')

# Using render to return html file
def introduction(request):
    return render(request, 'hello.html', { 'name': 'Luna', 'age': 5})

# Using render to return html file
def play_draughts(request):
        # Your logic to generate the board data goes here
    board = [
        [{'value': row * 10 + col + 1, 'dark': (row + col) % 2 == 0} for col in range(10)]
        for row in range(10)
    ]
    return render(request, 'draughts.html', {'board': board})