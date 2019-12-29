from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Welcome(Page):
    pass


class Inst_Part1WP(WaitPage):
    # def after_all_players_arrive(self):
    pass


class Inst_Part1(Page):
    pass


page_sequence = [
    Welcome,
    Inst_Part1WP,
    Inst_Part1
]
