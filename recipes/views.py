from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import Recipe, RecipeIngredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm

@login_required
def recipe_list_view(request):
    qs = Recipe.objects.filter(user=request.user)
    
    context = {'object_list':qs}
    return render(request, "recipes/list.html", context)

@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {'object':obj}
    return render(request, "recipes/detail.html", context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST)
    context = {
        'form':form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('blogs')
    return render(request, "recipes/create.html", context)

@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST, instance=obj)
    context = {
        'form': form,
        'obj': obj,
    }
    if form.is_valid():
        form.save()
        context['mesage'] = 'Data Saved'
        return redirect('blogs')
    return render(request, "recipes/update.html", context)   