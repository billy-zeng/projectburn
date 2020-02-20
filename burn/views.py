from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from requests_auth import Basic

# 'https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={your app_id}&app_key={your app_key}'
def home(request):
    # response = requests.get('https://foodapi.calorieking.com/v1', auth=('user', ''))
    response = requests.get('https://api.edamam.com/api/food-database/parser?ingr=red%20apple&app_id={9b687b99}&app_key={bc5f2cc77eb479801a3ec37121ccc27a}')
    data = response.json()
    print(response)
    return render(request, 'home.html', {
        'ip': data
    })

def dashboard(request):
    return render(request, 'dashboard.html')


# #This sets up the https connection
# c = HTTPSConnection("www.foodapi.calorieking.com/v1")
# #we need to base 64 encode it
# #and then decode it to acsii as python 3 stores it as a byte string
# userAndPass = b64encode(b"username:password").decode("ascii")
# headers = { 'Authorization' : '' %  userAndPass }
# #then connect
# c.request('GET', '/', headers=headers)
# #get the response back
# res = c.getresponse()
# # at this point you could check the status etc
# # this gets the page text
# data = res.read()
