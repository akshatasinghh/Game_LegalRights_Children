#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question

def quiz_view(request):
    questions = list(Question.objects.all())
    score = request.session.get('score', 0)
    question_num = request.session.get('question_num', 0)
    
    if question_num >= len(questions):
        return render(request, "quiz/result.html", {"score": score})
    
    question = questions[question_num]
    
    if request.method == "POST":
        selected_answer = request.POST.get("answer")
        if selected_answer == question.correct_answer:
            score += 1
        request.session['score'] = score
        request.session['question_num'] = question_num + 1
        return redirect("quiz_view")
    
    context = {
        "question": question,
        "question_num": question_num + 1,
        "total_questions": len(questions),
    }
    return render(request, "quiz/templates/quiz/quiz.html", context)
    try:
        get_template("quiz/quiz.html")
        return render(request, "quiz/quiz.html", {})
    except TemplateDoesNotExist:
        return HttpResponse("Template quiz/quiz.html not found!")
