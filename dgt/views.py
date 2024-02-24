from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django_hv.http import hv_reponde

from core.mobile import get_app

from .models import Question, SessionQuestion, SessionTest, Test
from .utils import get_or_create_session

APP = get_app("dgt")


def test_index(request):
    context = {"obj": APP, "tests": Test.objects.all()}
    xml_or_html = "xml" if request.hv else "html"
    return render(request, f"dgt/index.{xml_or_html}", context)


def question_detail(request, id):
    question = Question.objects.get(id=id)
    context = {"obj": APP, "question": question}
    if request.hv:
        return hv_reponde(render(request, "dgt/question.xml", context))
    return render(request, "dgt/question.html", context)


@csrf_exempt
def check_question(request, id):
    question = Question.objects.get(id=id)
    session, request = get_or_create_session(request)
    SessionQuestion.objects.create(
        question=question,
        session=session,
        selected_option=request.POST.get("selected_option", ""),
        test=question.test,
    )
    context = {"obj": APP, "question": question}

    if request.method == "GET":
        return redirect(question.detail_url)

    next_or_done = "next" if question.has_next else "done"
    xml_or_html = "xml" if request.hv else "html"
    if not question.has_next:
        session_test = SessionTest.objects.create(session=session, test=question.test)
        session_questions = SessionQuestion.objects.filter(
            test=question.test, session=session, session_test__isnull=True
        )
        session_questions.update(session_test=session_test)
        context["session_test"] = session_test
        context["tests"] = Test.objects.all()

    return render(request, f"dgt/{next_or_done}.{xml_or_html}", context)
