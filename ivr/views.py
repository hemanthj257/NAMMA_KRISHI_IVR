from django.http import HttpResponse
from twilio.twiml.voice_response import VoiceResponse, Gather, Dial
from .models import CallLog


def ivr_welcome(request):
    response = VoiceResponse()
    gather = Gather(num_digits=1, action='/gather_1/', method='POST', timeout=10)
    gather.say("Hello, Welcome to Namma Krishi, your ultimate destination to rent agricultural machines. "
               "Press 1 for renting a machine Press 2 to know the current details of rented machines Press 3 for Customer support")
    response.append(gather)
    
    # Add a fallback for no input
    response.say("We didn't receive your input. Goodbye.")
    response.hangup()
    return HttpResponse(str(response), content_type='text/xml')


def gather_1(request):
    digits = request.POST.get('Digits')
    response = VoiceResponse()

    if digits == '1':
        gather = Gather(num_digits=1, action='/gather_locality/', method='POST', timeout=10)
        gather.say("Please say the locality you live in to find the nearest lessor. Press 1 for Bangalore Press 2 for Mysuru Press 3 for Gadag")
        response.append(gather)
        response.say("We didn't receive your input. Goodbye.")
        response.hangup()
    else:
        response.say("This feature is under development. Goodbye.")
        response.hangup()
    return HttpResponse(str(response), content_type='text/xml')


def gather_locality(request):
    digits = request.POST.get('Digits')
    response = VoiceResponse()

    if digits == '1':
        response.say("You have selected Bangalore. Available lessor: ")
        gather = Gather(num_digits=1, action='/gather_brand/', method='POST', timeout=10)
        gather.say("Press 1 for Suntec Agrimart Press 2 for Sonalika, Banashankari Press 3 for Krishi Jagran, Sanjay Nagar")
        response.append(gather)
        response.say("We didn't receive your input. Goodbye.")
        response.hangup()
    else:
        response.say("Invalid selection. Goodbye.")
        response.hangup()
    return HttpResponse(str(response), content_type='text/xml')


def gather_brand(request):
    digits = request.POST.get('Digits')
    response = VoiceResponse()

    if digits == '1':
        response.say("You have selected Suntec Agrimart, Guddadahalli.")
        gather = Gather(num_digits=1, action='/gather_type/', method='POST', timeout=10)
        gather.say("Press 1 to rent farming vehicles. Press 2 to rent vehicle attachments.")
        response.append(gather)
        response.say("We didn't receive your input. Goodbye.")
        response.hangup()
    else:
        response.say("This item is currently not available. Goodbye.")
        response.hangup()
    return HttpResponse(str(response), content_type='text/xml')


def gather_type(request):
    digits = request.POST.get('Digits')
    response = VoiceResponse()

    if digits == '1':
        gather = Gather(num_digits=1, action='/connect_farming_vehicle/', method='POST', timeout=10)
        gather.say("Press 1 to rent tractors.")
        response.append(gather)
        response.say("We didn't receive your input. Goodbye.")
        response.hangup()
    elif digits == '2':
        gather = Gather(num_digits=1, action='/connect_attachments/', method='POST', timeout=10)
        gather.say("Press 1 for other farming vehicles.")
        response.append(gather)
        response.say("We didn't receive your input. Goodbye.")
        response.hangup()
    else:
        response.say("Invalid option. Goodbye.")
        response.hangup()
    return HttpResponse(str(response), content_type='text/xml')


def connect_farming_vehicle(request):
    response = VoiceResponse()

    try:
        # Store the call log
        CallLog.objects.create(
            call_sid=request.POST.get('CallSid', ''),
            from_number=request.POST.get('From', ''),
            to_number=request.POST.get('To', ''),
            status=request.POST.get('CallStatus', ''),
            direction=request.POST.get('Direction', ''),
            duration=request.POST.get('CallDuration', '0')
        )
    except Exception as e:
        # Log error but don't break the flow
        pass

    response.say("Connecting your call to the farming vehicle provider.")
    dial = Dial(timeout=30)
    dial.number("+917483544099")
    response.append(dial)
    return HttpResponse(str(response), content_type='text/xml')


def connect_attachments(request):
    response = VoiceResponse()

    try:
        CallLog.objects.create(
            call_sid=request.POST.get('CallSid', ''),
            from_number=request.POST.get('From', ''),
            to_number=request.POST.get('To', ''),
            status=request.POST.get('CallStatus', ''),
            direction=request.POST.get('Direction', ''),
            duration=request.POST.get('CallDuration', '0')
        )
    except Exception as e:
        # Log error but don't break the flow
        pass

    response.say("Connecting your call to the attachment provider.")
    dial = Dial(timeout=30)
    dial.number("+917483544099")
    response.append(dial)
    return HttpResponse(str(response), content_type='text/xml')
