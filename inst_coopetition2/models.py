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


author = 'Manu Munoz'

doc = """
Instructions 2: Preferences for Cooperation or Competition
"""


class Constants(BaseConstants):
    name_in_url = 'inst_coopetition2'
    players_per_group = None
    num_rounds = 1
    fixed_pay = 10
    exp_currency = "USD dollars"
    correct_pay = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
