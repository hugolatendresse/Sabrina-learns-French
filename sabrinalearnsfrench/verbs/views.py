from django.http import HttpResponse
from django.shortcuts import render
from .models import Verb  # Adjust this import according to your model's actual location
from django.db.models import F

from .models import Verb


# Create your views here.
def index(request):
    verb_list = Verb.objects.order_by("?")[:3]
    output =  "Today's verbs are:\n" + " \n ".join([v.francais for v in verb_list])
    return HttpResponse(output)

    # TODO
    # # Pass the random verbs to your template
    # context = {
    #     'verbs': random_verbs
    # }
    # return render(request, 'your_template_name.html', context)
