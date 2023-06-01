from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('trees/', views.arbor_index, name='arbor-index'),
  path('trees/<int:tree_id>/', views.arbor_detail, name='tree-detail'),
  path('trees/create/', views.TreeCreate.as_view(), name='arbor-create'),
  path('trees/<int:pk>/update/', views.TreeUpdate.as_view(), name='tree-update'),
  path('trees/<int:pk>/delete/', views.TreeDelete.as_view(), name='tree-delete'),
  path('trees/<int:tree_id>/add-season/', views.add_season, name='add-season'),
  path('pref/create/', views.PrefCreate.as_view(), name='pref-create'),
  path('prefs/<int:pk>/', views.PrefDetail.as_view(), name='pref-detail'),
  path('prefs/', views.PrefList.as_view(), name='pref-index'),
    path('prefs/<int:pk>/update/', views.PrefUpdate.as_view(), name='pref-update'),
  path('prefs/<int:pk>/delete/', views.PrefDelete.as_view(), name='pref-delete'),
  path('trees/<int:tree_id>/assoc-pref/<int:pref_id>/', views.assoc_pref, name='assoc-pref'),
  path('accounts/signup/', views.signup, name='signup'),
]