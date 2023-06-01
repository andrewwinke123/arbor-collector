from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .models import Tree, Pref
from .forms import SeasonForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('arbor-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

class TreeCreate(CreateView):
  model = Tree
  fields = ['name', 'family', 'description', 'lifeSpan']
  success_url = '/trees/'
  def form_valid(self, form):
    form.instance.user = self.request.user 
    return super().form_valid(form)

class TreeUpdate(UpdateView):
  model = Tree
  fields = ['family', 'description', 'lifeSpan']

class TreeDelete(DeleteView):
  model = Tree
  success_url = '/trees/'

class Home(LoginView):
  template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

def arbor_index(request):
  trees = Tree.objects.filter(user=request.user)
  return render(request, 'trees/index.html', { 'trees': trees })

def arbor_detail(request, tree_id):
  tree = Tree.objects.get(id=tree_id)
  prefs_tree_doesnt_have = Pref.objects.exclude(id__in = tree.prefs.all().values_list('id'))
  season_form = SeasonForm()
  return render(request, 'trees/detail.html', { 'tree': tree, 'season_form': season_form, 'prefs': prefs_tree_doesnt_have })

def add_season(request, tree_id):
  form = SeasonForm(request.POST)
  if form.is_valid():
    new_season = form.save(commit=False)
    new_season.tree_id = tree_id
    new_season.save()
  return redirect('tree-detail', tree_id=tree_id)

class PrefCreate(CreateView):
  model = Pref
  fields = '__all__'

class PrefList(ListView):
  model = Pref

class PrefDetail(DetailView):
  model = Pref

class PrefUpdate(UpdateView):
  model = Pref
  fields = ['name', 'color']

class PrefDelete(DeleteView):
  model = Pref
  success_url = '/prefs/'

def assoc_pref(request, tree_id, pref_id):
  Tree.objects.get(id=tree_id).prefs.add(pref_id)
  return redirect('tree-detail', tree_id=pref_id)