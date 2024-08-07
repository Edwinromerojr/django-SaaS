from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm

# Create your views here.
@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            link = form.save(commit=False)
            link.created_by = request.user
            link.save()

            return redirect('/')
    else:
        form = CategoryForm()

    return render(request, 'link/create_category.html', {'form': form})
