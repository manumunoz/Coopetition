from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

import time


class Intro(Page):

    def is_displayed(self):
        self.participant.vars['ra'] = self.player.gen_random_alphabet()
        print('Intro:',self.participant.vars['ra'])

        self.player.random_char_1  = list(self.participant.vars['ra'].keys())[ 0]
        self.player.random_char_2  = list(self.participant.vars['ra'].keys())[ 1]
        self.player.random_char_3  = list(self.participant.vars['ra'].keys())[ 2]
        self.player.random_char_4  = list(self.participant.vars['ra'].keys())[ 3]
        self.player.random_char_5  = list(self.participant.vars['ra'].keys())[ 4]
        self.player.random_char_6  = list(self.participant.vars['ra'].keys())[ 5]
        self.player.random_char_7  = list(self.participant.vars['ra'].keys())[ 6]
        self.player.random_char_8  = list(self.participant.vars['ra'].keys())[ 7]
        self.player.random_char_9  = list(self.participant.vars['ra'].keys())[ 8]
        self.player.random_char_10 = list(self.participant.vars['ra'].keys())[ 9]
        self.player.random_char_11 = list(self.participant.vars['ra'].keys())[10]
        self.player.random_char_12 = list(self.participant.vars['ra'].keys())[11]
        self.player.random_char_13 = list(self.participant.vars['ra'].keys())[12]
        self.player.random_char_14 = list(self.participant.vars['ra'].keys())[13]
        self.player.random_char_15 = list(self.participant.vars['ra'].keys())[14]
        self.player.random_char_16 = list(self.participant.vars['ra'].keys())[15]
        self.player.random_char_17 = list(self.participant.vars['ra'].keys())[16]
        self.player.random_char_18 = list(self.participant.vars['ra'].keys())[17]
        self.player.random_char_19 = list(self.participant.vars['ra'].keys())[18]
        self.player.random_char_20 = list(self.participant.vars['ra'].keys())[19]
        self.player.random_char_21 = list(self.participant.vars['ra'].keys())[20]
        self.player.random_char_22 = list(self.participant.vars['ra'].keys())[21]
        self.player.random_char_23 = list(self.participant.vars['ra'].keys())[22]
        self.player.random_char_24 = list(self.participant.vars['ra'].keys())[23]
        self.player.random_char_25 = list(self.participant.vars['ra'].keys())[24]
        self.player.random_char_26 = list(self.participant.vars['ra'].keys())[25]

        self.player.random_code_1  = list(self.participant.vars['ra'].values())[ 0]
        self.player.random_code_2  = list(self.participant.vars['ra'].values())[ 1]
        self.player.random_code_3  = list(self.participant.vars['ra'].values())[ 2]
        self.player.random_code_4  = list(self.participant.vars['ra'].values())[ 3]
        self.player.random_code_5  = list(self.participant.vars['ra'].values())[ 4]
        self.player.random_code_6  = list(self.participant.vars['ra'].values())[ 5]
        self.player.random_code_7  = list(self.participant.vars['ra'].values())[ 6]
        self.player.random_code_8  = list(self.participant.vars['ra'].values())[ 7]
        self.player.random_code_9  = list(self.participant.vars['ra'].values())[ 8]
        self.player.random_code_10 = list(self.participant.vars['ra'].values())[ 9]
        self.player.random_code_11 = list(self.participant.vars['ra'].values())[10]
        self.player.random_code_12 = list(self.participant.vars['ra'].values())[11]
        self.player.random_code_13 = list(self.participant.vars['ra'].values())[12]
        self.player.random_code_14 = list(self.participant.vars['ra'].values())[13]
        self.player.random_code_15 = list(self.participant.vars['ra'].values())[14]
        self.player.random_code_16 = list(self.participant.vars['ra'].values())[15]
        self.player.random_code_17 = list(self.participant.vars['ra'].values())[16]
        self.player.random_code_18 = list(self.participant.vars['ra'].values())[17]
        self.player.random_code_19 = list(self.participant.vars['ra'].values())[18]
        self.player.random_code_20 = list(self.participant.vars['ra'].values())[19]
        self.player.random_code_21 = list(self.participant.vars['ra'].values())[20]
        self.player.random_code_22 = list(self.participant.vars['ra'].values())[21]
        self.player.random_code_23 = list(self.participant.vars['ra'].values())[22]
        self.player.random_code_24 = list(self.participant.vars['ra'].values())[23]
        self.player.random_code_25 = list(self.participant.vars['ra'].values())[24]
        self.player.random_code_26 = list(self.participant.vars['ra'].values())[25]

        self.participant.vars['rw'] = self.player.gen_random_word(self.participant.vars['ra'])
        print('Intro:',self.participant.vars['rw'])

        self.player.word_char_1 = self.participant.vars['rw'][0]
        self.player.word_char_2 = self.participant.vars['rw'][1]
        self.player.word_char_3 = self.participant.vars['rw'][2]

        self.participant.vars['so'] = self.player.get_solution(self.participant.vars['ra'],self.participant.vars['rw'])
        print('Intro:',self.participant.vars['so'])

        if not 'total_trials' in self.participant.vars.keys():
            self.participant.vars['total_trials'] = 0
        # end if
        if not 'good_trials' in self.participant.vars.keys():
            self.participant.vars['good_trials'] = 0
        # end if
        if not 'bad_trials' in self.participant.vars.keys():
            self.participant.vars['bad_trials'] = 0
        # end if

        return self.round_number == 1
    # end def

    def before_next_page(self):
        self.participant.vars['expiry'] = time.time() + Constants.max_time
    # end def

# end class


class Play(Page):

    form_model = 'player'

    form_fields = [
        'word_code_1',
        'word_code_2',
        'word_code_3'
    ]

    timer_text = 'Time left in trial:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    # end def

    def is_displayed(self):
        if time.time() > self.participant.vars['expiry']:
            return False
        else:
            if self.round_number > Constants.num_rounds:
                return False
            else:
                return True
            # end if
        # end if
    # end def

    def before_next_page(self):
        sol = self.participant.vars['so']
        wc1 = int(self.player.word_code_1)
        wc2 = int(self.player.word_code_2)
        wc3 = int(self.player.word_code_3)
        print('SysSolution:',sol)
        print('UsrSolution:',[wc1,wc2,wc3])
        self.participant.vars['total_trials'] += 1
        if (sol[0] == wc1) and (sol[1] == wc2) and (sol[2] == wc3):
            self.participant.vars['good_trials'] += 1
        else:
            self.participant.vars['bad_trials'] += 1
        # end if
        print('self.participant.vars.total_trials =',self.participant.vars['total_trials'])
        print('self.participant.vars.good_trials  =',self.participant.vars['good_trials'] )
        print('self.participant.vars.bad_trials  =',self.participant.vars['bad_trials']  )
    # end def

# end class


class Results(Page):

    def is_displayed(self):
        self.player.total_codes = self.participant.vars['total_trials']
        self.player.good_codes  = self.participant.vars['good_trials']
        self.player.bad_codes   = self.participant.vars['bad_trials']
        return self.round_number >= Constants.num_rounds
    # end def

# end class


page_sequence = [
    Intro,
    Play,
    Results
]
