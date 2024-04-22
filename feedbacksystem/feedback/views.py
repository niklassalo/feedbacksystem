from django.shortcuts import render, redirect
from .forms import FeedbackForm

# Create your views here.

def home(request):
    return render(request, 'feedback/home.html')

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_success')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/submit_feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback/feedback_success.html')