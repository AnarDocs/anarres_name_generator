import string
import random

class NamesGenerator:
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    CONSONANTS = list(set(string.ascii_lowercase) - set(VOWELS))
    CONSONANTS_TO_AVOID = ['c', 'h', 'j', 'q', 'w', 'x', 'y']
    COMBINED_CONSONANTS = ['ch', 'gv', 'kv', 'sh']
    COMBINED_CONSONANTS_FOR_PART = {
        'begin': ['sk', 'tr'],
        'middle': ['rd', 'rr', 'rz', 'ss'],
        'end': ['ks']
    }
    NON_VOWEL_SOUNDS = list(set(CONSONANTS) - set(CONSONANTS_TO_AVOID)) + COMBINED_CONSONANTS
    NON_VOWEL_SOUNDS_FOR_PART = {
        'begin': NON_VOWEL_SOUNDS + COMBINED_CONSONANTS_FOR_PART['begin'],
        'middle': NON_VOWEL_SOUNDS + COMBINED_CONSONANTS_FOR_PART['middle'],
        'end': NON_VOWEL_SOUNDS + COMBINED_CONSONANTS_FOR_PART['end']
    }

    @classmethod
    def generate_name(cls):
        name = (
            random.choice(cls.NON_VOWEL_SOUNDS_FOR_PART['begin']) +
            random.choice(cls.VOWELS) +
            random.choice(cls.NON_VOWEL_SOUNDS_FOR_PART['middle']) +
            random.choice(cls.VOWELS) +
            random.choice(cls.NON_VOWEL_SOUNDS_FOR_PART['end'])
        )
        return name.capitalize()

    @classmethod
    def name(cls):
        # names should be 5 or 6 letters long
        while True:
            proposal = cls.generate_name()
            if len(proposal) == 5 or len(proposal) == 6:
                break

        # todo: check of name already given to living person
        # todo: check if non-dictionary-word

        return proposal

for _ in range(10):
    print(NamesGenerator.name())
