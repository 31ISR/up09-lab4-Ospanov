from django.shortcuts import render

# Create your views here.

def communities(req):
  return render(req, 'communities/commu.html')