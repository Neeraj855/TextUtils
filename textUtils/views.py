#-----------------------------------------------#
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the Text FROM User
    djtext = request.POST.get('text', 'default')

    # Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newline = request.POST.get('newline', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    countchar = request.POST.get('countchar', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {
            "purpose": 'Remove Punctuations',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if(fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {
            "purpose": 'Changed to Uppercase',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if(newline == 'on'):
        analyzed = ''
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {
            "purpose": 'Removed New Lines',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if(extraspaceremove == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {
            "purpose": 'Removed Extra Spaces',
            'analyzed_text': analyzed
        }
        djtext = analyzed
    if(countchar == 'on'):
        analyzed = ''
        count = 0
        for char in djtext:
            count = count+1
            analyzed = count
        params = {
            "purpose": 'Number of Characters',
            'analyzed_text': analyzed
        }
    if((removepunc != 'on') and (fullcaps != 'on') and (newline != 'on') and (extraspaceremove != 'on') and (countchar != 'on')):
        return HttpResponse('Please select an option... <a href="/">Back</a>')
    # else:
    return render(request, 'analyze.html', params)
