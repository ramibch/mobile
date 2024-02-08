from django.shortcuts import render, redirect

from django_hv.http import hv_reponde

from .models import Test, Question, SessionQuestion, SessionTest

from .utils import get_or_create_session


def test_index(request):
    context = {"tests": Test.objects.all()}
    if request.hv:
        return hv_reponde(render(request, "index.xml", context))
    return render(request, "index.html", context)


def app_info(request):
    donation_links = {
        "PayPal": "https://www.paypal.com/paypalme/ramiboutas",
        "buymeacoffee.com": "https://www.buymeacoffee.com/ramiboutas",
    }
    context = {
        "author": "Rami Boutassghount",
        "author_url": "https://ramiboutas.com/bio/",
        "donation_text": "Si te gusta la aplicación y quieres apoyar mi trabajo, puedes hacer una pequeña donación:",
        "donation_links": donation_links,
        "credits_text": "Los tests de esta aplicación están extraidos de la página oficial de la DGT.",
        "credits_url": "https://revista.dgt.es/",
    }
    if request.hv:
        return hv_reponde(render(request, "info.xml", context))
    return render(request, "info.html", context)


def question_detail(request, id):
    question = Question.objects.get(id=id)
    context = {"question": question}
    if request.hv:
        return hv_reponde(render(request, "question.xml", context))
    return render(request, "question.html", context)


def check_question(request, id):
    question = Question.objects.get(id=id)
    session, request = get_or_create_session(request)
    SessionQuestion.objects.create(
        question=question,
        session=session,
        selected_option=request.POST.get("selected_option", ""),
        test=question.test,
    )
    context = {"question": question}
    if not question.has_next:
        session_test = SessionTest.objects.create(session=session, test=question.test)
        session_questions = SessionQuestion.objects.filter(
            test=question.test, session=session, session_test__isnull=True
        )
        session_questions.update(session_test=session_test)
        # context["session_questions"] = session_questions
        context["session_test"] = session_test
        context["tests"] = Test.objects.all()

    if request.hv:
        return hv_reponde(render(request, "next.xml", context))
    return render(request, "next.html", context)
