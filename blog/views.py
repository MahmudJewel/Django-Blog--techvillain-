from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http.request import QueryDict

from blog import models as BMODEL
# from blog import forms as BFORM
# Create your views here.

def search_view(request):
    search=''
    searchItem = BMODEL.blogPost.objects.all()
    total_searchItem=searchItem.count() # for counting total in pagination
    if request.method == 'POST':
        search = request.POST.get('search')
        # print(f"search : {search}")
        searchItem = BMODEL.blogPost.objects.filter(title__contains = search)
        total_searchItem=searchItem.count() # for counting total in pagination
    # for Paginator 
    page = request.GET.get('page', 1)
    paginator = Paginator(searchItem, 6)  #6 objects in each page.
    try:
	    searchItem = paginator.page(page)
    except PageNotAnInteger:
	    searchItem = paginator.page(1)
    except EmptyPage:
	    searchItem = paginator.page(paginator.num_pages)
    context={
        'searchItem':searchItem,
        'search':search,
        'total_searchItem':total_searchItem,
    }
    return render(request, 'home/search.html',context)


def home_view(request):
    categories = BMODEL.category.objects.all()
    blogs = BMODEL.blogPost.objects.all().order_by('-date')[:4]
    context= {
        'categories' : categories,
        'blogs' : blogs,
    }
    return render(request, 'home/home.html', context)


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
    return render(request, 'blog/article_page.html', context)
