from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'courses/index.html')

# def register(request):
#     #logic to be added here
#     return redirect('login_page')
#
# def login(request):
#     #logic to be added here
#     return redirect('login_page')
