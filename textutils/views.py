# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check if we got the values
    rempunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    analysed = ""

    # Analyse the text, check which checkbox is on
    if rempunc == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punc:
                analysed += char

        djtext = analysed
        analysed = ""
    
    if fullcaps == 'on':
        for char in djtext:
            analysed += char.upper()

        djtext = analysed
        analysed = ""

    if newlineremove == 'on':
        for char in djtext:
            if char != '\n' and char != '\r':   # '\r' is because in network both are used to express a newline
                analysed += char

        djtext = analysed
        analysed = ""
    
    if extraspaceremove == 'on':
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not(djtext[index] == " "):
                    analysed += char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analysed += char

        djtext = analysed
        analysed = ""
    
    params = {
        'analysed_text': djtext
    }
    
    return render(request, 'analyse.html', params)
    

# Not yet ready maybe add later :P
def contact(request):
    # return render(request, 'contact.html')
    pass

def about(request):
    pass

# I have added this new line to the project on 12-10-2023
