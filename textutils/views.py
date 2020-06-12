from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def analyze(request):
    
    djtext = request.GET.get('text','default')

    
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    removespace = request.GET.get('removespace', 'off')
    removeline = request.GET.get('removeline', 'off')
    countchar = request.GET.get('charcount', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    
    punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~{}'''
    analyzed = ""

    if removepunc == 'on':
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        djtext = analyzed

    if capitalize == 'on':
        analyzed = djtext.title()
        djtext = analyzed

    if removespace == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed += char
        djtext = analyzed
    if removeline == 'on':
        analyzed = ""
        
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = djtext.upper()

    if countchar == 'on':
        sum = 0
        for char in djtext:
            if not(char == ' ' or char == '\n' or char == '\r'):
                sum += 1
        analyzed += "\n Total Characters are "
        analyzed += str(sum)

    if(removepunc != 'on' and capitalize != 'on' and removespace != 'on' and removeline != 'on' and  fullcaps != 'on' and countchar != 'on'):
            analyzed += "Please Select any Operation and try again !"
    params = {'purpose': '', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
