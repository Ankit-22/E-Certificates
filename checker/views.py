from django.shortcuts import render
from django.http import HttpResponse

from creator.models import Certificate

# Create your views here.

def test(request):
	return HttpResponse("Hello, World!")

def show_certificate(request, certificate_hash):
	certificate = ""
	try:
		certificate = Certificate.objects.get(certificate_identifier = certificate_hash)
	except Certificate.DoesNotExist:
		return HttpResponse("404 Not Found")
	except Certificate.MultipleObjectsReturned:
		print("This is impossible")
		return HttpResponse("400 Bad Request")
	except:
		print("Don't expect this")
	return HttpResponse(certificate.certificate_event.event_name)
