from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from sets import Set
from xml.dom import minidom
from django.template import Context
import json
import inspect, os
import math
import copy
import re

# Create your views here.

def index(request):
    #template = loader.get_template('vepp4journal/index.html')
    #return HttpResponse(template.render())
    return HttpResponse("I'm VEPP4 Journal, hello!")