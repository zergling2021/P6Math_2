from django import forms

class ReceiveAnswer(forms.Form):
    answer_returned = forms.DecimalField(help_text="Enter Your Answer")
    