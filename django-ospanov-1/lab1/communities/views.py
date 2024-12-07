from django.shortcuts import render, get_object_or_404
from .models import Community

def communities(request):
  communities = Community.objects.all().order_by('-date')
  return render(request, 'communities/communities.html', {'communities': communities})

def communities_page(request, slug):
    community = get_object_or_404(Community, slug=slug)
    return render(request, 'communities/communities_page.html', {'community': community})
