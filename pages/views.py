from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm
# Create your views here.
def home_view(request):
    return render(request, "home.html")

def about_view(request):
    return render(request, "pages/about.html")



def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            html_message = render_to_string(
                'emails/contact.html',
                {'name': name, 'email': email, 'message': message}

            )


            send_mail(
                subject="New Contact Form Submission",
                message=message,
                from_email=email,
                recipient_list=['duskibrad@gmail.com'],
                html_message=html_message

            )

    form = ContactForm()
    return render(request, 'contact.html', {'form': form})