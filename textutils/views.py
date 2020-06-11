# I Have Created This Website
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

def analyze(request):

    # Getting The Text
 # if request.method == "post":
    djtext = request.POST.get('text','default')

    # Checking the checkbox
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    removespace = request.POST.get('removespace', 'off')
    removeline = request.POST.get('removeline', 'off')
    countchar = request.POST.get('charcount', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    # string = ""
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
        # analyzed = djtext.replace('\n','').replace('\r','')
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
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
    # return HttpResponse(s)
#
# def capfirst(request):
#     s = '''<a href = "/">Back to main</a>'''
#     return HttpResponse(s)
#
# def newlineremove(request):
#     s = '''<a href = "/">Back to main</a>'''
#     return HttpResponse(s)
#
# def spaceremove(request):
#     s = '''<a href = "/">Back to main</a>'''
#     return HttpResponse(s)
#
# def charcount(request):
#     s = '''<a href = "/">Back to main</a>'''
#     return HttpResponse(s)
