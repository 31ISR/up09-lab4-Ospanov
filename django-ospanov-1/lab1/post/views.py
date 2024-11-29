from django.shortcuts import render

# Create your views here.


def post_list(req):
  return render(req, 'post/post_list.html')