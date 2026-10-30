from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import logging

from .models import Course, Lesson, Enrollment, Question, Choice, Submission

logger = logging.getLogger(__name__)


# Course list view
class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-total_enrollment')[:10]


# Course detail view
class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_details_bootstrap.html'


# Enroll in course view
def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    if user.is_authenticated:
        Enrollment.objects.get_or_create(user=user, course=course)
        return redirect('onlinecourse:course_details', pk=course.id)
    return redirect('onlinecourse:login')


# Registration view
def registration_request(request):
    context = {}
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('onlinecourse:index')
        context['registration_form'] = form
    else:
        context['registration_form'] = UserCreationForm()
    return render(request, 'onlinecourse/user_registration_bootstrap.html', context)


# Login view
def login_request(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onlinecourse:index')
        context['error'] = "Invalid username or password."
    return render(request, 'onlinecourse/user_login_bootstrap.html', context)


# Logout view
def logout_request(request):
    logout(request)
    return redirect('onlinecourse:index')


# <HINT> Create a submit view to handle exam submission:
# - Check if request is POST
# - Get the course and current user's enrollment
# - Create a new Submission instance
# - Collect selected choices from POST request
# - Add selected choices to the submission instance
# - Redirect to show_exam_result view
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        # Retrieve enrollment for logged in user
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        # Create a new Submission object
        submission = Submission.objects.create(enrollment=enrollment)
        # Extract selected choice IDs from POST request (name="choice")
        selected_ids = request.POST.getlist('choice')
        # Add selected choices to the submission's ManyToMany field
        for choice_id in selected_ids:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
        # Redirect to show_exam_result view
        return redirect('onlinecourse:show_exam_result', course_id=course.id, submission_id=submission.id)
    return redirect('onlinecourse:course_details', pk=course.id)


# <HINT> Create a show_exam_result view to display exam results:
# - Get the course and submission objects
# - Calculate total score based on selected choices
# - Render exam_result_bootstrap.html with context
def show_exam_result(request, course_id, submission_id):
    context = {}
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    total_score = 0
    questions = course.question_set.all()
    selected_choices = submission.choices.all()
    selected_ids = [c.id for c in selected_choices]
    
    for question in questions:
        if question.is_get_score(selected_ids):
            total_score += question.grade

    context['course'] = course
    context['submission'] = submission
    context['grade'] = total_score
    context['selected_ids'] = selected_ids
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

