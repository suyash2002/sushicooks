from django.urls import path
from .views import RecipeDetailView, RecipeListView,RecipeCreateView,RecipeUpdateView,RecipeDeleteView

urlpatterns = [  
    path('new/',RecipeCreateView.as_view(),name="recipe_new"),
    path('', RecipeListView.as_view(), name="recipes_home"),
    path('<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
    path('<int:pk>/update/',RecipeUpdateView.as_view(),name="recipe_edit"),
    path('<int:pk>/delete/',RecipeDeleteView.as_view(),name="recipe_delete"),
]