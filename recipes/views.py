from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from recipes.models import Recipe
from django.urls import reverse_lazy
class RecipeListView(ListView):
  model=Recipe
  template_name='index.html'

class RecipeDetailView(DetailView):
  model=Recipe
  template_name='recipe_detail.html'
  
class RecipeCreateView(CreateView):
      model=Recipe
      fields='__all__'
      template_name='recipe_new.html'
    
class RecipeUpdateView(UpdateView):
      model=Recipe
      template_name='recipe_edit.html'
      fields=['title','body']

class RecipeDeleteView(DeleteView):
      model=Recipe
      template_name='recipe_delete.html'
      success_url=reverse_lazy('home')
    
           