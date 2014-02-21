#coding:utf-8

from django.contrib.auth import *
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.conf import settings
#from datetime import datetime
#import os
#import time
#import bs4
#import datetime, calendar 


