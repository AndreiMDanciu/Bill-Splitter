from django.shortcuts import render
from .forms import *

# Create your views here.

# def home(request):
#     return render(request, 'bill_app/home.html')

def split_bill(request):
    result = None

    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            total = form.cleaned_data['bill']
            tip = int(form.cleaned_data['tip'])
            people = form.cleaned_data['people']

            tip_amount = total * tip / 100
            total_with_tip = total + tip_amount
            per_person = total_with_tip / people

            result = {
                'tip_amount': round(tip_amount, 2),
                'total_with_tip': round(total_with_tip, 2),
                'per_person': round(per_person, 2),
            }
    else:
        form = BillForm()
    
    return render(request, 'bill_app/home.html', {'form': form, 'result': result})

