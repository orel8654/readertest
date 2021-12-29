from pprint import pprint
from django.shortcuts import render
from reader.models import ItemsParsed

def index(request):
    row = ItemsParsed.objects.filter(brand='Limon4')[:4]
    rows = {
        'row': row,
    }
    return render(request, template_name='reader/index.html', context=rows)