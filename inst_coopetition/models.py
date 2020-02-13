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
Instructions: Preferences for Cooperation or Competition
"""


class Constants(BaseConstants):
    name_in_url = 'inst_coopetition'
    players_per_group = None
    num_rounds = 1
    fixed_pay = 10
    total_pay = 20
    exp_currency = "USD dollars"
    correct_pay = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.PositiveIntegerField(
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other']
        ],
        widget=widgets.RadioSelect
    )

    age = models.IntegerField (min=18, max=100)

    education = models.PositiveIntegerField(
        choices=[
            [1, 'Less than high school'],
            [2, 'High school diploma or equivalent (e.g., GED)'],
            [3, 'Some college'],
            [4, 'College diploma'],
            [5, 'Masters degree'],
            [6, 'Professional post-secondary degree or doctoral degree (e.g., JD, MD, PhD etc.)'],
        ],
        widget=widgets.RadioSelect
    )


    state = models.PositiveIntegerField(
        choices=[
            [1, ' Alabama '],
            [2, ' Alaska '],
            [3, ' Arizona '],
            [4, ' Arkansas '],
            [5, ' California '],
            [6, ' Colorado '],
            [7, ' Connecticut '],
            [8, ' Delaware '],
            [9, ' District of Columbia '],
            [10, ' Florida '],
            [11, ' Georgia '],
            [12, ' Hawaii '],
            [13, ' Idaho '],
            [14, ' Illinois '],
            [15, ' Indiana '],
            [16, ' Iowa '],
            [17, ' Kansas '],
            [18, ' Kentucky '],
            [18, ' Louisiana '],
            [19, ' Maine '],
            [20, ' Maryland '],
            [21, ' Massachusetts '],
            [22, ' Michigan '],
            [23, ' Minnesota '],
            [24, ' Mississippi '],
            [25, ' Missouri '],
            [26, ' Montana '],
            [27, ' Nebraska '],
            [28, ' Nevada '],
            [29, ' New Hampshire '],
            [30, ' New Jersey '],
            [31, ' New Mexico '],
            [32, ' New York '],
            [33, ' North Carolina '],
            [34, ' North Dakota '],
            [35, ' Ohio '],
            [36, ' Oklahoma '],
            [37, ' Oregon '],
            [38, ' Pennsylvania '],
            [39, ' Rhode Island '],
            [40, ' South Carolina '],
            [41, ' South Dakota '],
            [42, ' Tennessee '],
            [43, ' Texas '],
            [44, ' Utah '],
            [45, ' Vermont '],
            [46, ' Virginia '],
            [47, ' Washington '],
            [48, ' Washington DC'],
            [49, ' West Virginia '],
            [50, ' Wisconsin '],
            [51, ' Wyoming '],
        ],
    )

    income = models.PositiveIntegerField(
        choices=[
            [1, 'Less than $10,000'],
            [2, '$10,000 - $19,999'],
            [3, '$20,000 - $29,999'],
            [4, '$30,000 - $39,999'],
            [5, '$40,000 - $49,999'],
            [6, '$50,000 - $59,999'],
            [7, '$60,000 - $69,999'],
            [8, '$70,000 - $79,999'],
            [9, '$80,000 - $99,999'],
            [10, '$100,000 - $119,999'],
            [11, '$120,000 - $149,999'],
            [12, '$150,000 - $199,999'],
            [13, '$200,000 -'],
            [14, 'I do not wish to report my income.'],
        ],
        widget=widgets.RadioSelect
    )
