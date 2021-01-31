from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse

from .forms import EnquiryForm
from .models import Enquiry


def hello_world(request):
    """ View function for hello world. """
    context = {
        'greetings': 'hello, world!',
    }
    return render(request, 'hello_world.html', context=context)


def links(request):
    """ View function for links. """
    from portfolio.urls import urlpatterns
    context = {
        'pages': [
            pattern.name for pattern in urlpatterns
        ],
    }
    return render(request, 'links.html', context=context)


def portfolio(request):
    """ View function for profile page. """
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Enquiry.objects.create(sender=sender, subject=subject, message=message)
            return HttpResponseRedirect(reverse('thanks'))
    else:
        form = EnquiryForm()

    context = {
        'projects': """
[**Song Lyrics & Popularity API**](https://github.com/KooCook/slap)

  - RESTful API integrating song information, popularity, and lyrics together.
  - Integrated data from Genius, Wikidata, Spotify and YouTube APIs.
  - Visualized song data using d3.js and plotly.
  - Analyzed song data using the scipy stack.


[**Movies Award Ontology**](https://github.com/th-bunratta/MovieAwardOntologyMAO)

  - Ontology describing movies and awards with focus on individuals from IMDb and Wikidata.
  - Created modules for data processing and auto-generating documentation.
  - Designed data flow of the application.
  - Utilised spaCy NLP to process unclean semistructured data.


[**KEMI Project**](https://github.com/kemi-kun/KEMI)

  - Prolog program for nomenclature of inorganic chemical compounds.
  - Translated rules in the IUPAC Red Book to first-order logic in prolog.


[**KooCook**](https://github.com/KooCook/koocook-dj)

  - Web app for searching and publishing recipes with auto-calculated nutrition information
  - Developed module to handle structured data.
  - Utilised USDA’s FoodData API to get nutrition information for processing.


[**Musicality**](https://github.com/MaiMee1/musicality)

  - Music game compatible with .osu levels file format used in the rhythm game Osu!.
  - Developed GUI application using arcade and pyglet.
""",
        'hobbies': """
For music I play the piano, violin, guitar, ขิม, and ขลุ่ย, but mostly piano.  


For sports I used to play golf. Now I don't do anything exercise related except weight traning.  


For entertainment I go to YouTube. I watch cooking, science, maths, devs related things, drama/tea, philosophy, skincare, and many other things.   
Some of my favorite people/channels are: Crash Course, scishow, KatBlaque, ContraPoints, Hyram, PhilosophyTube, America's Test Kitchen, and much more


I like gaming but don't really have time for that anymore. I'm also into online novels, mangas/manhuas, and webtoons. 
""",
        'form': form
    }
    return render(request, 'portfolio.html', context=context)


def thanks(request):
    return render(request, 'thanks.html')
