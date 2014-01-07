from django.shortcuts import render
from zend.settings import STATIC_URL
from django.http import HttpResponse
from polls.models import Poll
from django.template import RequestContext,loader
def index(request):
    latest_poll_list=Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context=RequestContext(request,{'latest_poll_list':latest_poll_list,})
   
    return HttpResponse(template.render(context))
def detail(request,poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)
def results(request,poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)
def vote(request,poll_id):
    return HttpResponse("youre voting on poll %s." %poll_id)
#def loginpage(request):
#    static_url=STATIC_URL
 #   return render_to_response('admin/login.html',locals())

# Create your views here.
