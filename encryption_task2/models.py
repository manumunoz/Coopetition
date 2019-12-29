from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

author = 'Manu Munoz'

doc = """
Encryption task 2 for Preferences for Cooperation or Competition
"""

class Constants(BaseConstants):
    name_in_url= 'encryption_task2'
    players_per_group = None
    num_rounds= 300
    max_time= 60.0 #5.0 * 60.0
# end class

class Subsession(BaseSubsession):
    pass
# end class

class Group(BaseGroup):
    pass
# end class

class Player(BasePlayer):

    random_char_1  = models.StringField(label='',initial='')
    random_char_2  = models.StringField(label='',initial='')
    random_char_3  = models.StringField(label='',initial='')
    random_char_4  = models.StringField(label='',initial='')
    random_char_5  = models.StringField(label='',initial='')
    random_char_6  = models.StringField(label='',initial='')
    random_char_7  = models.StringField(label='',initial='')
    random_char_8  = models.StringField(label='',initial='')
    random_char_9  = models.StringField(label='',initial='')
    random_char_10 = models.StringField(label='',initial='')
    random_char_11 = models.StringField(label='',initial='')
    random_char_12 = models.StringField(label='',initial='')
    random_char_13 = models.StringField(label='',initial='')
    random_char_14 = models.StringField(label='',initial='')
    random_char_15 = models.StringField(label='',initial='')
    random_char_16 = models.StringField(label='',initial='')
    random_char_17 = models.StringField(label='',initial='')
    random_char_18 = models.StringField(label='',initial='')
    random_char_19 = models.StringField(label='',initial='')
    random_char_20 = models.StringField(label='',initial='')
    random_char_21 = models.StringField(label='',initial='')
    random_char_22 = models.StringField(label='',initial='')
    random_char_23 = models.StringField(label='',initial='')
    random_char_24 = models.StringField(label='',initial='')
    random_char_25 = models.StringField(label='',initial='')
    random_char_26 = models.StringField(label='',initial='')

    random_code_1  = models.IntegerField(label='',initial=0)
    random_code_2  = models.IntegerField(label='',initial=0)
    random_code_3  = models.IntegerField(label='',initial=0)
    random_code_4  = models.IntegerField(label='',initial=0)
    random_code_5  = models.IntegerField(label='',initial=0)
    random_code_6  = models.IntegerField(label='',initial=0)
    random_code_7  = models.IntegerField(label='',initial=0)
    random_code_8  = models.IntegerField(label='',initial=0)
    random_code_9  = models.IntegerField(label='',initial=0)
    random_code_10 = models.IntegerField(label='',initial=0)
    random_code_11 = models.IntegerField(label='',initial=0)
    random_code_12 = models.IntegerField(label='',initial=0)
    random_code_13 = models.IntegerField(label='',initial=0)
    random_code_14 = models.IntegerField(label='',initial=0)
    random_code_15 = models.IntegerField(label='',initial=0)
    random_code_16 = models.IntegerField(label='',initial=0)
    random_code_17 = models.IntegerField(label='',initial=0)
    random_code_18 = models.IntegerField(label='',initial=0)
    random_code_19 = models.IntegerField(label='',initial=0)
    random_code_20 = models.IntegerField(label='',initial=0)
    random_code_21 = models.IntegerField(label='',initial=0)
    random_code_22 = models.IntegerField(label='',initial=0)
    random_code_23 = models.IntegerField(label='',initial=0)
    random_code_24 = models.IntegerField(label='',initial=0)
    random_code_25 = models.IntegerField(label='',initial=0)
    random_code_26 = models.IntegerField(label='',initial=0)

    word_char_1    = models.StringField(label='',initial='')
    word_char_2    = models.StringField(label='',initial='')
    word_char_3    = models.StringField(label='',initial='')

    word_code_1    = models.IntegerField(label='',initial=0)
    word_code_2    = models.IntegerField(label='',initial=0)
    word_code_3    = models.IntegerField(label='',initial=0)

    total_words    = models.IntegerField(label='',initial=0)
    good_words     = models.IntegerField(label='',initial=0)
    bad_words      = models.IntegerField(label='',initial=0)

    def gen_random_alphabet(self):
        alphabet = []
        anumbers = []
        alphanum = {}
        for i in range(26):
            alphabet.append(chr(i+65))
        # end for
        random.shuffle(alphabet)
        while True:
            n = random.randint(100,999)
            if not n in anumbers:
                anumbers.append(n)
            # end if
            if len(anumbers) >= 100:
                break
            # end if
        # end while
        for i in range(len(alphabet)):
            alphanum[alphabet[i]] = anumbers[i]
        # end for

        return alphanum
    # end def

    def gen_random_word(self,ra):
        randword = []
        while True:
            rl = random.randint(0,25)
            if not rl in randword:
                randword.append(rl)
            # end if
            if len(randword) >= 3:
                break
            # end if
        # end while
        for i in range(len(randword)):
            randword[i] = list(ra.keys())[randword[i]]
        # end for
        return randword
    # end def

    def get_solution(self,ra,rw):
        solution = []
        for l in rw:
            solution.append(ra[l])
        # end for
        return solution
    # end def

# end class
