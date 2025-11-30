RPG_ERROR = {'narration': 'Map name does not match save file',
             'inspection': 'Map name does not match save file',
             'encounter': 0}

RPG_OUTOFBOUNDS = {'narration': 'You only see vast sea where you are trying to go.',
                   'inspection': 'You smell salt.'}


SCORCHED = {'narration': "The land that surrounds you is scorched. No life could ever live here.",
            'inspection': "you feel as though you are being watched.",
            'biome': 'scorched',
            'encounter': 5}

FIELDS = {'narration': "You stand in a vast field. The ground beneath you is as green as emerald.",
          'inspection': "You only notice the warmth of the sun on your face.",
          'biome': 'fields',
          'encounter': 15}

DESERT = {'narration': "You find yourself in a dry desert. It would take a hearty person to survive these lands.",
          'inspection': "You kick the sand around to find only more sand.",
          'biome': 'desert',
          'encounter': 10}

test_map = [[SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, DESERT, FIELDS, FIELDS, FIELDS, FIELDS, DESERT, SCORCHED],
            [SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED, SCORCHED]
            ]

rpg_map_list = ['test_map']