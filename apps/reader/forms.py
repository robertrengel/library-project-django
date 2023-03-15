from django import forms
from .models import Loan
from apps.book.models import Book

class LoanForm(forms.ModelForm):

    class Meta:
        model = Loan
        fields = (
            "reader",
            "book"
        )
        
class MultipleLoanForm(forms.ModelForm):
    
    books = forms.ModelMultipleChoiceField(
        queryset= None,
        required=True,
        widget =forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Loan
        fields = ("reader",)
    
    def __init__(self, *args, **kwargs):
        super(MultipleLoanForm, self).__init__(*args, **kwargs)
        self.fields['books'].queryset = Book.objects.all()