# #from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from .models import Question

# def quiz_view(request):
#     questions = list(Question.objects.all())
#     score = request.session.get('score', 0)
#     question_num = request.session.get('question_num', 0)
    
#     if question_num >= len(questions):
#         return render(request, r"C:\Users\aksha\OneDrive\Documents\7th Semester\PCL\ChildrenRights_GAME\legal_rights_quiz\quiz\templates\result.html", {"score": score})
    
#     question = questions[question_num]
    
#     if request.method == "POST":
#         selected_answer = request.POST.get("answer")
#         if selected_answer == question.correct_answer:
#             score += 1
#         request.session['score'] = score
#         request.session['question_num'] = question_num + 1
#         return redirect("quiz_view")
    
#     context = {
#         "question": question,
#         "question_num": question_num + 1,
#         "total_questions": len(questions),
#     }
#     return render(request, r"C:\Users\aksha\OneDrive\Documents\7th Semester\PCL\ChildrenRights_GAME\legal_rights_quiz\quiz\templates\quiz.html", context)
#     try:
#         get_template("quiz/quiz.html")
#         return render(request, "quiz/quiz.html", {})
#     except TemplateDoesNotExist:
#         return HttpResponse("Template quiz/quiz.html not found!")


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question

def quiz_view(request):
    # Retrieve questions and session variables
    questions = list(Question.objects.all())
    score = request.session.get('score', 0)
    question_num = request.session.get('question_num', 0)

    # Check if quiz is completed
    if question_num >= len(questions):
        return render(request, "result.html", {"score": score, "total_questions": len(questions)})

    # Current question
    question = questions[question_num]

    # Handle POST request (answer submission)
    if request.method == "POST":
        selected_answer = request.POST.get("answer")
        if selected_answer == question.correct_answer:
            score += 1
        request.session['score'] = score
        request.session['question_num'] = question_num + 1
        return redirect("quiz_view")  # Redirect to the next question

    # Render the quiz page with the current question
    context = {
        "question": question,
        "question_num": question_num + 1,
        "total_questions": len(questions),
    }
    return render(request, "quiz.html", context)


# def retry_quiz(request):
#     """Clear session data to restart the quiz."""
#     request.session['score'] = 0
#     request.session['question_num'] = 0
#     return redirect("quiz_view")


def retry_quiz(request):
    """Clear session data to restart the quiz."""
    # Reset session variables
    request.session['score'] = 0
    request.session['question_num'] = 0

    # Redirect to the quiz start page
    return redirect("quiz_view")

