
from django.http import HttpResponse
from django.shortcuts import render

import operator


def home(request):
    return render(request, 'home.html' , {'hithere':"Hi this is me"})


def count(request):

    fulltext = request.GET['sometext']

    wordlist = fulltext.split()

    wordcount = len(wordlist)


    worddict = {}
    for word in wordlist:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1

    worddict = sorted(worddict.items(), key=operator.itemgetter(1), reverse = True)
    return render(request,'count.html', {'fulltext': fulltext, 'wordcount': wordcount, 'worddictionary': worddict})

