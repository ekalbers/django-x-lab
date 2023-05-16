from django.views.generic import ListView, CreateView
from .models import Food
from django.urls import reverse_lazy


class FoodListView(ListView):
    template_name = 'food/food_list.html'
    model = Food
    context_object_name = 'food_list'


class FoodCreateView(CreateView):
    template_name = 'food/food_create.html'
    model = Food
    fields = ['name', 'price', 'owner']
    success_url = reverse_lazy('food-list')
