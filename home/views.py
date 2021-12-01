from django.shortcuts import render
from blog import models as BMODEL
# Create your views here.

def home_view(request):
    blogs = BMODEL.blogPost.objects.all()
    singleBlog = BMODEL.blogPost.objects.all().first()
    if request.method=='GET':
        dc=request.GET
        pk=dc.get('id')
        print(type(pk))
        if pk != None :
            singleBlog = BMODEL.blogPost.objects.get(id=pk)
        # print(f"type of get: {type(request.GET)}" )
        # print(f"get methods are : {dc.get('id')}")
        context= {
        'blogs':blogs,
        'singleBlog' : singleBlog,
    }
    return render(request, 'home/home.html', context)
