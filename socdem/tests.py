from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    def play_round(self):
        yield (pages.Socdem_Quest,
               {'gender': random.randint(1, 3), 'age': 22, 'education': 1, 'state': 1, 'income': 1})