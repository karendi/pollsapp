from django.shortcuts import render
from django.http import Http404
from . import models


def homepage(request):
    title = "Welcome enter your county to get started"
    return render(request, 'homepage.html', {'title': title})


def searchcounty(request):
    if request.method == 'GET':
        # first return the presidential candidates
        query = request.GET.get("countyname")
        country = 'Kenya'
        presidents = models.President.objects.filter(Country__Name__contains= country)
        try:
            governors = models.Governor.objects.filter(County__Name__contains=query)
            senators = models.Senator.objects.filter(County__Name__contains= query)
            womenreps = models.Womensrep.objects.filter(County__Name__contains= query)
            constituencies = models.Constituency.objects.filter(County__Name__contains= query)
        except:
            raise Http404("the information for the county has not been entered yet")
        return render(request,'list.html',
                      dict(presidents=presidents, governors=governors, senators=senators, womenreps=womenreps,
                           constituencies=constituencies , query=query))
