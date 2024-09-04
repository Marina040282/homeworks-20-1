from django.shortcuts import render
from django.views.generic import ListView
from models import Product
# Create your views here.


#def index(request, *args, **kwargs):
#    return render(request, 'catalog/app_name/index.html')
class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        # get_queryset - запрос на выборку данных из БД
        queryset = super().get_queryset()
        return queryset



def contacts(request, *args, **kwargs):
    return render(request, 'catalog/app_name/contacts.html')
