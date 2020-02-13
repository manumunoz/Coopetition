from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass

class Socdem_QuestWP(WaitPage):
    pass

class Socdem_Quest(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'education', 'state', 'income']

    def age_error_message(self, value):
        is_correct = (value >= 18)
        if not (is_correct):
            return 'You must be at least 18 years old to participate in this study.'

class Inst_Part1WP(WaitPage):
    pass

class Inst_Part1(Page):
    pass


page_sequence = [
    Welcome,
    Socdem_QuestWP,
    Socdem_Quest,
    Inst_Part1WP,
    Inst_Part1
]
