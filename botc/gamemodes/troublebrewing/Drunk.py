"""Contains the Drunk Character class"""

import json 
import random
from botc import Outsider, Character, Townsfolk
from ._utils import TroubleBrewing, TBRole

with open('botc/gamemodes/troublebrewing/character_text.json') as json_file: 
    character_text = json.load(json_file)[TBRole.drunk.value.lower()]

class Drunk(Outsider, TroubleBrewing, Character):
    """Drunk: You think you are a Townsfolk, but your ability malfunctions.

    ===== DRUNK ===== 

    true_self = drunk
    ego_self = [townsfolk] *persistent
    social_self = drunk

    commands
    - None

    initialize setup? -> NO
    initialize role? -> YES

    override first night instruction? -> NO  # default is to send instruction string only
    override regular night instruction -> NO  # default is to send nothing
    """

    def __init__(self):
        
        Character.__init__(self)
        TroubleBrewing.__init__(self)
        Outsider.__init__(self)

        self._desc_string = character_text["description"]
        self._examp_string = character_text["examples"]
        self._instr_string = character_text["instruction"]
        self._lore_string = character_text["lore"]
        
        self._art_link = "http://bloodontheclocktower.com/wiki/images/0/03/Drunk_Token.png"
        self._wiki_link = "http://bloodontheclocktower.com/wiki/Drunk"

        self._role_enum = TBRole.drunk
        self._emoji = "<:drunk:722687457828798515>"
    
    def exec_init_role(self, setup):
        """Randomly choose a townsfolk that is not in play. (persistent throughout the game)"""
        possibilities = [role_class() for role_class in TroubleBrewing.__subclasses__() if issubclass(role_class, Townsfolk)]
        taken = [player.role.name for player in setup.townsfolks]
        random.shuffle(possibilities)
        for p in possibilities:
            if p.name not in taken:
                self._ego_role = p
        