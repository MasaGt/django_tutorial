from django.test import TestCase
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
