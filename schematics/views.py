from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse
from .models import schematics
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    if request.GET.get("id"):
        id = request.GET.get("id")
        schematic = schematics.objects.filter(id=id).values()
        if not schematic:
            raise Http404
        else:
            schematicPage = loader.get_template('schematicPage.html')
            model = schematics.objects.get(id=id)
            model.downloadCountHR = human_format(model.downloadCount)
            model.save()
            context = {
                'schematic': schematic,
            }
            return HttpResponse(schematicPage.render(context, request))
    if request.GET.get('page'):
        schematicsList = schematics.objects.all().values()
        pages = Paginator(schematicsList, 10)
        page_number = request.GET.get('page') 
        try:
            page_obj = pages.get_page(page_number)  # returns the desired page object
        except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
            page_obj = pages.page(1)
        except EmptyPage:
        # if page is empty then return last page
            page_obj = pages.page(0)
        context = {
            'page_content' : page_obj,
            'schematic': schematicsList
        }
        index = loader.get_template('index.html')
        return HttpResponse(index.render(context, request))
    if request.GET.get('search'):
        query = request.GET.get("search")
        model = schematics
        return schematics.objects.filter(
            Q(title__icontains=query) | Q(shortDescription__icontains=query)
        )
    else:
        index = loader.get_template('index.html')
        schematicsList = schematics.objects.all().values().order_by("-currentDateTime")
        context = {
            'schematics': schematicsList
        }
        return HttpResponse(index.render(context, request))

def increment_download_count(request, id):
    schematic = schematics.objects.filter(id=id).values()
    if not schematic:
        raise Http404
    else:
        model = schematics.objects.get(id=id)
        model.downloadCount += 1
        model.save()
        return HttpResponseRedirect(model.fileLink)

def human_format(num):
    if num < 1000:
        return str(num)
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])