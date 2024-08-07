from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from link.models import Link

# Create your views here.
@login_required
def dashboard(request):
    newest_links = Link.objects.filter(created_by=request.user)[0:5]
    return render(request, 'dashboard/dashboard.html', {
        'newest_links': newest_links
    })