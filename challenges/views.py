from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def monthly_challenges(request,month):
    challenge_text = None
    if month == "january":
        challenge_text = "JANUARY"
    elif month == "february":
        challenge_text = "FEBRUARY"
    elif month == "march":
        challenge_text = "MARCH"
    elif month == "april":
        challenge_text = "APRIL"
    elif month == "may":
        challenge_text = "MAY"
    elif month == "june":
        challenge_text = "JUNE"
    elif month == "july":
        challenge_text = "JULY"
    elif month == "august":
        challenge_text = "AUGUST"
    elif month == "september":
        challenge_text = "SEPTEMBER"
    elif month == "october":
        challenge_text = "OCTOBER"
    elif month == "november":
        challenge_text = "NOVEMBER"
    elif month == "december":
        challenge_text = "DECEMBER"
    else:
        return HttpResponseNotFound("This month is not supported!")

    return HttpResponse(challenge_text)  
    

