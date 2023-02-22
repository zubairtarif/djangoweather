#This is my views.py file
from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		
		api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ str(zipcode) + "&distance=5&API_KEY=2F6C4CD8-7F12-40F2-B9D0-BC97E0AE5D03") # api_request is an arbitrary name

		try:
			api = json.loads(api_request.content)

		except Exception as e:
			api = "Error..."

		#api.0.Category.Name This is how html references	
		if api[1]['Category']['Name'] == "Good":
			category_description = "0-50. Air condition seems satisfactory."
			category_color = "good"
		elif api[1]['Category']['Name'] == "Moderate":
			category_description = "51-100. Air condition seems moderate."
			category_color = "moderate"
		elif api[1]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "101-150. Air condition may be unhealthy for sensitive groups."
			category_color = "usg"
		elif api[1]['Category']['Name'] == "Unhealthy":
			category_description = "151-200. Air condition is unhealthy."
			category_color = "unhealthy"
		elif api[1]['Category']['Name'] == "Very Unhealthy":
			category_description = "201-300. Air condition is VERY unhealthy."
			category_color = "veryunhealthy"
		elif api[1]['Category']['Name'] == "Hazardous":
			category_description = "301-500. Health warnings of emergency conditions."
			category_color = "hazardous"


		return render(request, 'home.html', {'api':api,
			'category_description':category_description,
			'category_color': category_color })




	else:	
		return render(request, 'home.html', {'api':"<Enter Zip Code>",
			'category_description':"",
			'category_color': "good" })



def about(request):
	return render(request, 'about.html', {})


