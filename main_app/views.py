from django.shortcuts import render

# Add the following import
from django.http import HttpResponse


class Tree:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

trees = [
  Tree('Lolo', 'tabby', 'Kinda rude.', 3),
  Tree('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
  Tree('Fancy', 'bombay', 'Happy fluff ball.', 4),
  Tree('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def arbor_index(request):
  return render(request, 'trees/index.html', { 'trees': trees })