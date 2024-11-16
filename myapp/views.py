from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import redirect
from .models import ButtonClick
from django.shortcuts import HttpResponseRedirect
from urllib.parse import urlencode


# myapp/views.py


def home(request):
    return render(request, 'index.html')  # Replace 'home.html' with your template name

def record_click(request, button_type):
    if button_type in ['location', 'contact']:
        ButtonClick.objects.create(button_type=button_type)
    return HttpResponseRedirect("https://maps.app.goo.gl/t7QN4JcyVY18dETv6")  # Redirect to a page after recording click

#aria-label="Chat on WhatsApp"
 #                       href="https://wa.me/196264565187?text=I'm%20interested%20in%20your%20car%20for%20sale"

def redirect_to_whatsapp(request, button_type):
    if button_type in ['location', 'contact']:
        ButtonClick.objects.create(button_type=button_type)

    # Define the WhatsApp phone number in international format
    phone_number = "6264565187"  # replace with actual number
    # Define a default message (optional)
    message = "Hello, I'm interested in your services!"
    
    # Encode the message to make it URL safe
    params = urlencode({"text": message})
    
    # Construct the WhatsApp URL
    whatsapp_url = f"https://wa.me/{phone_number}?{params}"
    
    # Redirect to WhatsApp URL
    return HttpResponseRedirect(whatsapp_url)


    ###def contact_gmail(request, button_type):
   
  #  ButtonClick.objects.create(button_type='contact')

    # Define the email details
   # recipient_email = "Mahaveerenterprisesindore@gmail.com"
   # subject = "Hello from Django!"
   # body = "This is a pre-filled email body. Feel free to modify it!"
    
    # Construct the mailto link with URL encoding
   # mailto_link = f"mailto:{recipient_email}?{urlencode({'subject': subject, 'body': body})}"
    
    # Pass the mailto link to the template
 #   return render(request, 'index.html', {'mailto_link': mailto_link})

def initiate_call(request, button_type):
    if button_type in ['location', 'contact']:
        ButtonClick.objects.create(button_type='contact')
    # Render the template and pass the tel link
    return render(request, 'contact.html')