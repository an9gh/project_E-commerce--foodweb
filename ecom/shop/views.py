from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.

def home(request,c_slug = None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404 (Categ,slug=c_slug)
        prodt = Products.objects.filter(category=c_page,available=True)

    else:

        prodt = Products.objects.all().filter(available=True)
    cat = Categ.objects.all()
    paginator = Paginator(prodt,7)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page =1
    try:
        pro = paginator.page(page)
    except(EmptyPage,InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request,'index.html',{'pr':prodt , 'ct':cat,'pg':pro})


def ProdDetailes(request,c_slug,product_slug):
    try:
        prod = Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html' , {'pr':prod})


def Searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
        
    return render(request, 'search.html', {'qr':query,'pr':prod})