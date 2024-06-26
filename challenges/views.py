from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def index(request):
  list_items = ""
  months=list(monthly_challenges.keys())
  
  for month in months:
    capitalize_month=month.capitalize()
    month_path = reverse("month-challenge",args=[month])
    list_items += f"<li><a href=\"{month_path}\">{capitalize_month}</a></li>"
  

  response_data = f"<ul>{list_items}</ul>"
  return HttpResponse(response_data)


monthly_challenges = {
  "january": "Wake up at 6 AM everyday for whole month!",
  "february": "Learn Django for 1 hour everyday for whole month!",
  "march": "Walk for at least 20 minutes everyday!",
  "april": "Read 1 chapter from any book everyday for whole month",
  "may": "Wake up at 6 AM everyday for whole month!",
  "june": "Learn Django for 1 hour everyday for whole month!",
  "july": "Walk for at least 20 minutes everyday!",
  "august": "Read 1 chapter from any book everyday for whole month",
  "september": "Wake up at 6 AM everyday for whole month!",
  "october": "Learn Django for 1 hour everyday for whole month!",
  "november": "Walk for at least 20 minutes everyday!",
  "december": "Learn Django for 1 hour everyday for whole month!"
}

def monthly_challenge_by_number(request, month):
  months = list(monthly_challenges.keys())

  if month > len(months):
    return HttpResponseNotFound("Invalid month")
  
  redirect_month = months[month - 1]
  redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge
  return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    response_data = f"<h1>{challenge_text}</h1>"
    return HttpResponse(response_data)
  except:
    return HttpResponseNotFound("<h1>This month is not supported yet!</h1>")

  # if month == 'january':
  #   challenge_text = "Wake up at 6 AM everyday for whole month!"
  # elif month == 'february':
  #   challenge_text = "Walk for at least 20 minutes everyday!"
  # elif month == 'march':
  #   challenge_text = "Learn Django for whole month!"
  # else:
  #   return HttpResponseNotFound("This month is not supported!")
  # return HttpResponse(challenge_text)