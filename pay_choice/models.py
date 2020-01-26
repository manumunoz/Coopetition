from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import itertools

author = 'Manu Munoz'

doc = """
Pay Choice: Preferences for Cooperation or Competition
"""


class Constants(BaseConstants):
    name_in_url = 'pay_choice'
    players_per_group = None
    num_rounds = 1
    fixed_pay = 10
    exp_currency = "USD dollars"
    correct_pay = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        treat = itertools.cycle([1, 2, 3, 4])
        # 1: EXO Comp, 2: EXO Coop, 3: ENDO Comp, 4: ENDO Coop
        # for p in self.get_players():
        #     p.treat = next(treat)
        for p in self.get_players():
            if 'treatment' in self.session.config:
                # demo mode
                p.treat = self.session.config['treatment']
            else:
                # live experiment mode
                p.treat = next(treat)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treat = models.IntegerField() # Treatments from 1 to 3

    endo = models.PositiveIntegerField(blank=True)

    def var_between_apps(self):
        self.participant.vars['endo'] = self.endo