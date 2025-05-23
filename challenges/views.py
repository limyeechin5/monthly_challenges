from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenge = {
    "january" : "JANUARY" ,
    "february" : "FEBRUARY" ,
    "march" : "MARCH" ,
    "april" : "APRIL" ,
    "may" : "MAY" ,
    "june" : "JUNE" ,
    "july" : "JULY" ,
    "august" : "AUGUST" ,
    "september" : "SEPTEMBER" ,
    "october" : "OCTOBER" ,
    "november" : "NOVEMBER" ,
    "december" : "DECEMBER" 
}

# Create your views here.
def monthly_challenges_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not support")
      
    

