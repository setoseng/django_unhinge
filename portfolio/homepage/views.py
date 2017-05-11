from django.template.response import TemplateResponse
from django import forms
from django import http
from django.core.mail import send_mail

from homepage.templates.forms import emailForm




def homepage (request):
  return TemplateResponse(request, 'homepage.html', {})



def contact_me(request):
	form = emailForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			send_mail(
    				'Hello',
    				'I would like to play a game...',
    				'contact@setyaseng.com',
    				[form.cleaned_data['your_email']],
    				fail_silently=False,
			)
			return http.HttpResponseRedirect('/thanks')
	context = {
		'form':form
	}
	return TemplateResponse(request, 'contact_me.html', context)

def thanks(request):
	return TemplateResponse(request, 'thanks.html' , {})


