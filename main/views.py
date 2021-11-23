from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail

from My_project.settings import RECIPIENT_ADDRESS



def index(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def prices(request):
	return render(request, 'main/prices.html')

def contact(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		phone = request.POST['phone']
		message = request.POST['message']


		#send an email
		send_mail(
			name, # subject
			message, # message
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
              # To Email

		)
		return render(request, 'main/contact.html', {})
	
	else:
		return render(request, 'main/contact.html', {})





def services(request):
	return render(request, 'main/services.html')

def sidebar_right(request):
	return render(request, 'main/sidebar_right.html')

def projects(request):
	return render(request, 'main/projects.html')

#def contact(request):
#	submitted = False
#	if request.method == 'POST':
#		form = ContactForm(request.POST)
#		if form.is_valid():
#			cd = form.clean_data
#			# assert False
#			con = get_connection('django.core.mail.backends.console.EmailBackend')
#			send_mail(
##				cd['subject'],
##				cd['message'],
#				cd.get('email', 'nathanielgleeson@yahoo.com'),
#				['nathanielgleeson@yahoo.com'],
#				connection=con
#			)
#			return HttpResponseRedirect('/contact?submitted=True')
#	else:
#		form = ContactForm()
#		if 'submitted' in request.GET:
#			submitted = True
#	return render(request, "main/contact.html", \
 #                     {"method": request.method})


