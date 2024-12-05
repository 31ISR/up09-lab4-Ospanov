from django.shortcuts import render
from .models import Community

def communities(request):
  communities = Community.objects.all().order_by('-date')
  return render(request, 'communities/commu.html', {'communities': communities})

