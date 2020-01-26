from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Payment(Page):
    def vars_for_template(self):
        return dict(
            endo=self.participant.vars['endo'],
            good_p1=self.participant.vars['good_codes'],
            good_p2=self.participant.vars['good_words'],
            points1= Constants.correct_pay * self.participant.vars['good_codes'],
            points2 = Constants.correct_pay * self.participant.vars['good_words'],
        )


page_sequence = [
    Payment,
]
