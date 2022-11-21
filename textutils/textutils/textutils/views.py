# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
#Get the text
      djtext = request.POST.get('text','default')
      removepunc = request.POST.get('removepunc','off')
      fullcaps =    request.POST.get('fullcaps','off')
      newlineremover =    request.POST.get('newlineremover','off')
      extraspaceremover = request.POST.get('extraspaceremover','off')
      charcount  = request.POST.get('charcount','off')

      if removepunc == "on":
          punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
          analyzed  = " "
          for char in djtext:
              if char not in punctuations:
                  analyzed = analyzed +' '+ char
          params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
          return render(request, "Analyze.html", params)


      elif fullcaps == 'on':
          analyzed = ""
          for char in djtext:
              analyzed = analyzed+char.upper()
          params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
          return render(request, "Analyze.html", params)


      elif newlineremover =='on':
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed+char
        params = {'purpose': 'Removed New Lines', 'analyzed_text':analyzed}
        return render(request, "Analyze.html", params)

      elif extraspaceremover == 'on':
          analyzed = " "
          for index,char in enumerate(djtext):
              if djtext[index] == " " and djtext[index+1] == " ":
                  pass
              else:
                  analyzed = analyzed + char
          params = {'purpose': 'Number of characters', 'analyzed_text': analyzed}
          return render(request, "Analyze.html", params)


      elif charcount == 'on':
          analyzed = ('No. of characters given in the text are :'+ str(len(djtext)))
          # analyzed = 0
          # for char in djtext:
          #     analyzed  = analyzed + 1
          params = {'purpose' : 'Number of characters','analyzed_text': analyzed}
          return render(request, "Analyze.html",params)



      else:
          return HttpResponse("Error")




# def ex1(request):
#        sites = ['''<h1> For Entertainment</h1><a href = "https://www.youtube.com">Youtube video</a>''',
#                 '''<h1> For Study </h1><a href = "https://www.google.com">Youtube video</a>'''

# def about(request):
#     return HttpResponse("About Shubham Bhai")

# def Main(request):
#     return HttpResponse("<h1>This is main menu of the site</h1>")

