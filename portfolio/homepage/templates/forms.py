from django import forms


class emailForm(forms.Form):
	your_name = forms.CharField(label="Your Name", max_length=100)
	your_email = forms.CharField(label="Your Email" , max_length=100)
	your_question = forms.CharField(label="Your Question", max_length=100)