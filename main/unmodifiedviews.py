from django.shortcuts import render, redirect




def index(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def prices(request):
	return render(request, 'main/prices.html')

#def contact(request):
#	return render(request, 'main/contact.html')

def services(request):
	return render(request, 'main/services.html')

def sidebar_right(request):
	return render(request, 'main/sidebar_right.html')

def projects(request):
	return render(request, 'main/projects.html')

#def contact(request):
#	if request.method == "POST":
#		message_name = request.POST["name"]
#		message_email = request.POST['email']
#		message_subject = request.POST['subject']
#		message_text = request.POST['text']
#		form = ContactForm()
#		context = {'form': form}
#		return render(request, 'main/contact.html', context)
#	else:
#		return render(request, "main/contact.html", {})

def contact(request):
    for name in request.POST:
        print("{}: {}".format(name, request.POST.getlist(name)))
    return render(request, "main/contact.html", \
        {"method": request.method})