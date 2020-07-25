from django.shortcuts import render
from django.http import HttpResponse

def post(request):
    posts = [
        {
            "title": "Post1",
            "text": "ahdshba",
            "created": "2020-07-18 10:39"
        },{
            "title": "Post2",
            "text": "buterbrod s sirom",
            "created": "2020-07-18 21:14"
        },{
            "title": "Post3",
            "text": "asdasd",
            "created": "2020-07-17 14:19"
        }
    ]
    return render(request, "post.html", { "data" : posts })
def index(request):
    return render(request, "index.html")
def comment(request):
    return render(request, "comment.html")
def about(request):
    return render(request, "about.html")
