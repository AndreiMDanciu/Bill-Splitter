from django import forms

tip_choices = [
    (0, '0%'),
    (5, '5%'),
    (10, '10%'),
    (15, '15%'),
    (20, '20%'),
]

class BillForm(forms.Form):
    bill = forms.DecimalField(label="Total Nota", min_value=0, decimal_places=2)
    tip = forms.ChoiceField(label='Bacsis (%)', choices=tip_choices, widget=forms.Select(attrs={'class': 'custom-select'}))   #widget e folosit pentru a putea adauga atribute variabilei, iar attrs este un dictionar tot pentru personificarea atributului
    people = forms.IntegerField(label='Numar persoane', min_value=1)
