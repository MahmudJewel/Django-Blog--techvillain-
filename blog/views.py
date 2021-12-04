from django.shortcuts import render

from django.http.request import QueryDict

from blog import models as BMODEL
# from blog import forms as BFORM
# Create your views here.

def search_view(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        print(f"search : {search}")
        searchItem = BMODEL.blogPost.objects.filter(title__contains = search)
    return render(request, 'home/search.html',{'searchItem':searchItem})


def home_view(request):
    return render(request, 'home/home.html')


def category_view(request, pk):
    blogs = BMODEL.blogPost.objects.filter(category=pk)
    singleBlog = blogs.first()  # get the first object
    # category heading for left side
    category = BMODEL.category.objects.get(id=pk)
    # print(f"category: {category}")
    # print(f"testing category from {category}")
    if request.method == 'GET':
        dc = request.GET
        pk = dc.get('getid')  # getid from url link
        # print(type(pk))
        if pk != None:
            singleBlog = BMODEL.blogPost.objects.get(id=pk)
        # print(f"type of get: {type(request.GET)}" )
        # print(f"get methods are : {dc.get('id')}")

    context = {
        'blogs': blogs,
        'singleBlog': singleBlog,
        'category': category,
        }
    return render(request, 'home/home.html', context)
