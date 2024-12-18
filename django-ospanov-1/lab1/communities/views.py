from django.shortcuts import render, get_object_or_404, redirect
from .models import Community
from django.contrib.auth.decorators import login_required

from . import forms 


def communities(request):
  communities = Community.objects.all().order_by('-date')
  return render(request, 'communities/communities.html', {'communities': communities})

def communities_page(request, slug):
    community = get_object_or_404(Community, slug=slug)
    return render(request, 'communities/communities_page.html', {'community': community})

@login_required(login_url="/users/login/")
def communities_new(request):
    form = forms.CreateCommunities(request.POST or None, request.FILES or None)
    if form.is_valid():
        newcommunities = form.save(commit=False)
        newcommunities.author = request.user
        newcommunities.save()
        return redirect('communities:list')

    return render(request, 'communities/communities_new.html', {'form': form})
