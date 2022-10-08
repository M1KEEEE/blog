from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
	now = datetime.now()
	return render(
		request, 
		"my_app/index.html", 
		{"is_new_year": now.day == 1 and now.month == 1})