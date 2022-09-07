from django.views.generic import ListView,DetailView
from recipes.models import Recipe

class RecipeList(ListView):
  model=Recipe
  template_name='index.html'

class RecipeDetailView(DetailView):
  model=Recipe
  template_name='recipe_detail.html'