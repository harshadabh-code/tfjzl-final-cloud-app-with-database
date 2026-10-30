# Online Course Application with Assessment Feature

This repository contains the Django-based Online Course application extended with an exam assessment feature for the IBM / Coursera Final Project: **Add a New Assessment Feature to an Online Course App**.

## Key Features Implemented
- **Models (`onlinecourse/models.py`)**: Added `Question`, `Choice`, and `Submission` models with scoring logic (`is_get_score`).
- **Admin (`onlinecourse/admin.py`)**: Registered models with `QuestionInline`, `ChoiceInline`, `QuestionAdmin`, and `LessonAdmin`.
- **Views (`onlinecourse/views.py`)**: Implemented `submit` and `show_exam_result` functions.
- **URLs (`onlinecourse/urls.py`)**: Configured URL routes for exam submission and result pages.
- **Templates (`onlinecourse/templates/onlinecourse/`)**: Created Bootstrap-styled templates `course_details_bootstrap.html` and `exam_result_bootstrap.html`.

## Submission Deliverables
- Task 1: `onlinecourse/models.py`
- Task 2: `onlinecourse/admin.py`
- Task 3: `screenshots/03-admin-site.png`
- Task 4: `onlinecourse/templates/onlinecourse/course_details_bootstrap.html`
- Task 5: `onlinecourse/views.py`
- Task 6: `onlinecourse/urls.py`
- Task 7: `screenshots/07-final.png`

