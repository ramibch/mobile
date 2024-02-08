from ..utils import get_or_create_session

from django import template

register = template.Library()

from ..models import SessionTest, Test


@register.simple_tag
def sessiontest_emojis(request, test: Test):
    session = get_or_create_session(request)[0]
    qs = SessionTest.objects.filter(test=test, session=session)[:5]
    return "".join(st.passed_emoji for st in qs)
