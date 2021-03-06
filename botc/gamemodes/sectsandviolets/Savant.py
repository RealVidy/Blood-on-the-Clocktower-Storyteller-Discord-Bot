"""Contains the Savant Character class"""

import json
from botc import Character, Townsfolk
from ._utils import SectsAndViolets, SnVRole

with open('botc/gamemodes/sectsandviolets/character_text.json') as json_file:
    character_text = json.load(json_file)[SnVRole.savant.value.lower()]


class Savant(Townsfolk, SectsAndViolets, Character):
    """Savant: Each day, you may visit the Storyteller to learn 2 things in private: 1 is true & 1 is false.
    """

    def __init__(self):

        Character.__init__(self)
        SectsAndViolets.__init__(self)
        Townsfolk.__init__(self)

        self._desc_string = character_text["description"]
        self._examp_string = character_text["examples"]
        self._instr_string = character_text["instruction"]
        self._lore_string = character_text["lore"]

        self._art_link = "https://bloodontheclocktower.com/wiki/images/4/4c/Savant_Token.png"
        self._wiki_link = "https://bloodontheclocktower.com/wiki/Savant"

        self._role_enum = SnVRole.savant
