from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":

		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = message_email + '' + request.POST['message']

		send_mail(
			message_name,
			message,
			message_email,
			['mjmacklin554@gmail.com'],
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name': message_name})



	else:

		return render(request, 'contact.html', {})
