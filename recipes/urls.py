from django.urls import path
from .views import RecipeDetailView, RecipeList

urlpatterns = [
    path('', RecipeList.as_view(), name="recipes_home"),
    path('<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
]