from django.shortcuts import render
from django.http import HttpResponse

from .tasks import TestTask
from django.core.mail import EmailMessage
from records.models import Event, Attendee
from records.utils import generate_event_url, get_event_by_url
from .utils import generate_hash
from .models import Certificate


# Create your views here.



def test(request):


	TestTask.delay("Hello, World!")



	return HttpResponse("Done!")


def make_cert(request, event_name):

	if request.method == 'GET':

		event_url = generate_event_url(event_name)
		event = get_event_by_url( event_url )

		for attendee in event.attendees.all():
			# Now generate model
			try:
				certificate = Certificate(certificate_identifier = generate_hash(attendee, event_name, event_url), certificate_holder = attendee, certificate_event = event)
				certificate.save()
			except:
				print("Already Created For This User")

		return HttpResponse("Welcome! ")