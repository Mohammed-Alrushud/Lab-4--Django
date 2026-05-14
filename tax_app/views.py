from django.http import HttpResponse

tax_rate = 0.15  # Store tax rate as a variable

def home(request):
    return HttpResponse("<p>This is a site to calculate tax.</p>")

def calculate(request, number):
    total = number * (1 + tax_rate)
    return HttpResponse(f"<p>Total price after tax: {total}</p>")

def taxrate(request):
    return HttpResponse(f"<h1>{tax_rate * 100}%</h1>")