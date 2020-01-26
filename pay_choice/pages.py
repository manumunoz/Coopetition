from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Choice(Page):
    form_model = 'player'
    form_fields = ['endo']

    def before_next_page(self):
        self.player.var_between_apps()


page_sequence = [
    Choice,
]
