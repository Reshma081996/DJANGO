from  django import forms

class EmployeeCreateForm(forms.Form):
    name=forms.CharField()
    designation=(
        ("developer","developer"),
        ("qa","qa"),
        ("hr","hr"),
        ("sales","sales")
    )

    designation=forms.ChoiceField(choices=designation)
    salary=forms.IntegerField()
    location=forms.CharField()
    email=forms.CharField()