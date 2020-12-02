from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from feedback.models import FeedbackModel

from feedback.form import FeedbackForm


# Create your views here.

def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            file = form.cleaned_data['file']
            f = FeedbackModel(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                message=message,
                file=file
            )
            f.save()
            return HttpResponseRedirect('/')
        else:
            print("Error")
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form})
