from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Route for course list
    path(route='', view=views.CourseListView.as_view(), name='index'),
    # Route for registration
    path('registration/', views.registration_request, name='registration'),
    # Route for login
    path('login/', views.login_request, name='login'),
    # Route for logout
    path('logout/', views.logout_request, name='logout'),
    # Route for course details
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # Route for enroll
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    # <HINT> Path for exam submission
    path('<int:course_id>/submit/', views.submit, name='submit'),
    # <HINT> Path for show_exam_result
    path('course/<int:course_id>/submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

