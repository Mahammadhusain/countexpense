from django import forms
from .models import *

class CreditForm(forms.ModelForm):
    class Meta:
        model = CreditModel
        fields = '__all__'
        widgets = {
            'amt':forms.NumberInput(attrs={'class':'form-control'}),
            'tag':forms.Select(attrs={'class':'form-control'}),
        }
        labels = {
            'amt':'Enter Amount For Credit',
            'tag':'Enter Tag For Credit Amount',
        }
        
class DebitForm(forms.ModelForm):
    class Meta:
        model = DebitModel
        fields = '__all__'
        widgets = {
            'amt':forms.NumberInput(attrs={'class':'form-control','id':'debit_amt'}),
            'tag':forms.Select(attrs={'class':'form-control','id':'debit_tag'}),
        }
        labels = {
            'amt':'Enter Amount For Debit',
            'tag':'Enter Tag For Debit Amount',
        }

class TransferForm(forms.ModelForm):
    class Meta:
        model = BankTransferModel
        fields = '__all__'
        widgets = {
            'amt':forms.NumberInput(attrs={'class':'form-control','id':'transfer_amt'}),
            'tag':forms.Select(attrs={'class':'form-control','id':'transfer_tag'}),
        }
        labels = {
            'amt':'Enter Amount For Debit',
            'tag':'Enter Tag For Debit Amount',
        }

class FastButtonForm(forms.ModelForm):
    class Meta:
        model = CreditDebitTransferButtonModel
        fields = '__all__'
        exclude = ['tag']
        widgets = {
            'amt':forms.NumberInput(attrs={'class':'form-control','id':'fast_amt'}),
            'tag':forms.TextInput(attrs={'class':'form-control','id':'fast_tag'}),
            'btn_type':forms.Select(attrs={'class':'form-control','id':'fast_btn_type'}),
        }
        labels = {
            'amt':'Enter Button Amount',
            'tag':'Enter Button info',
            
        }
