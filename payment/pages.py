from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Payment(Page):
    pass


page_sequence = [
    Payment,
]
