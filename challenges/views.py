from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

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
def monthly_challenges_index(request):
    months = list(monthly_challenge.keys())
    text = ""
    for m in months:
        capitalized_month = m.capitalize()
        redirect_path = reverse("month-challenge", args=[m])
        text += f"<li><a href=\"{redirect_path}\">{capitalized_month}</a></li>" + "\n\n"
    
    text = f"<ul>{text}</ul>"
    return HttpResponse(text)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid Month</h1>")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not support</h1>")
      




