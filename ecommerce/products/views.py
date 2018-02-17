
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView


from .models import Product
# Create your views here.


class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = "products/detail.html"


class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name =  'products/list.html'

class ProductDetailView(DetailView):
    #queryset = Product.objects.all()
    template_name = 'products/detail.html' 

    def get_object(self, *args, **kwargs):
        request = self.request
        print(request,"its request")
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product dosen't exist")
        return instance



class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        print(request)
        slug = self.kwargs.get('slug')
        print(slug)
        #instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Uhhmmm ")
        return instance