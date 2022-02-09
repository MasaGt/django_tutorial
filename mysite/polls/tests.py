from django.test import TestCase
from django.urls import reverse
import datetime
from django.utils import timezone
from polls.models import Question
# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_with_future_date(self):
        """
        question with future date should be returned False
        when was_published is call
        """
        future_date = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=future_date)
        self.assertIs(future_question.was_published(), False)

    def test_was_published_with_old_question(self):
        """
        quetion with past date should be returned True
        when was_published is call
        """
        time = timezone.now() - datetime.timedelta(days=1)
        old_quetion = Question(pub_date=time)
        self.assertIs(old_quetion.was_published(), True)


def create_question(content, days):
    """
    Create and return a Question Model

    Parameters
    ----------
    cnotent: str
        Text of a # QUESTION:
    days: datetime
        Offset to now
        (negative for questions published in the past,
         positive for questions that have yet to be published).
    """

    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(content=content, pub_date=time)
    return question


def access_by_get(test_class, url_name):
    """
    access url_name by get request

    Parameters
    ----------
    test_class: TestCase Class
        use it's client.get() to access a page by get
    url_name: str
        name argument of path function in urls.py
    """
    return test_class.client.get(reverse(url_name))


class ViewTests(TestCase):
    def test_index_view_with_get(self):
        """
        when an user access with '/polls/'
        there should be a page returned and response status is 200
        """
        response = self.client.get(reverse('polls:index'))
        self.assertIs(response.status_code, 200)

    def test_index_view_without_question(self):
        """
        Pass if 'Polls are not published' is showed
        """
        response = access_by_get(self, 'polls:index')
        self.assertContains(response, "Polls are not published")

    def test_reigster_past_question(self):
        """
        Pass if there is one question displayed
        """
        # call create_question before access_by_get
        question = create_question(
                            content="Question published in the past",
                            days=-30
                            )

        response = access_by_get(
                            self,
                            'polls:index')

        self.assertQuerysetEqual(
                            response.context['q_list'],
                            [question]
                            )

    def test_reigster_future_question(self):
        """
        Pass if 'Polls are not published' is showed
        """

        create_question(
                        content="Question will be published in the future",
                        days=30
                        )

        response = access_by_get(
                        self,
                        'polls:index'
                        )

        self.assertContains(
                        response,
                        "Polls are not published"
                        )

        def test_register_past_and_future_question(self):
            """
            Pass only if there is a past question displayed
            """

            response = access_by_get(self, 'polls:index')

            old_question = create_question(
                            content="Question published in the past",
                            days=-30
                            )

            create_question(
                            content="Question will be published in the future",
                            days=30
                            )

            self.assertConatins(
                            response.context['q_list'],
                            [old_question]
                            )

        def test_register_two_past_question(self):
            """
            Pass there is two quetions displayed
            """

            response = access_by_get(
                            self,
                            "polls:index"
                            )

            question1 = create_question(
                            content="old question1",
                            days=-20
                            )
            question2 = create_question(
                            content="old question2",
                            days=-10
                            )

            self.assertContains(
                            response.context['q_list'],
                            [question1, question2]
                            )
