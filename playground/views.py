from django.shortcuts import render
from store.models import Product,OrderItem,Order
from django.db.models.aggregates import Count,Min,Max,Sum
from tags.models import TaggedItem
from django.contrib.contenttypes.models import ContentType

def hello(request):
    TaggedItem.objects.get_tags_for(Product, 1)
     
    return render(request,'hello.html',)


