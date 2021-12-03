from django.shortcuts import render

from django.http.request import QueryDict

from blog import models as BMODEL
# from blog import forms as BFORM
# Create your views here.

def home_view(request):
    blogs = BMODEL.blogPost.objects.all()
    singleBlog = BMODEL.blogPost.objects.all().first() # get the first object
    category = BMODEL.category.objects.all()
    if request.method=='GET':
        dc=request.GET
        pk=dc.get('getid') # getid from url link
        # print(type(pk))
        if pk != None :
            singleBlog = BMODEL.blogPost.objects.get(id=pk)
        # print(f"type of get: {type(request.GET)}" )
        # print(f"get methods are : {dc.get('id')}")
        context= {
        'blogs':blogs,
        'singleBlog' : singleBlog,
        'category' : category,
    }
    return render(request, 'home/home.html', context)
