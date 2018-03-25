from django.shortcuts import render
from django.http import HttpResponse

from .tasks import TestTask
from django.core.mail import EmailMessage
from records.models import Event, Attendee
from records.utils import generate_event_url, get_event_by_url
from .utils import generate_hash


# Create your views here.



def test(request):


	TestTask.delay("Hello, World!")



	return HttpResponse("Done!")


def make_cert(request, event_name):

	if request.method == 'GET':

		event_url = generate_event_url(event_name)

		for attendee in get_event_by_url( event_url ).attendees.all():
			# Now generate model
			print(generate_hash(attendee, event_name, event_url))

		return HttpResponse("Welcome! ")