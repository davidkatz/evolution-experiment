import string
import fitness_functions

# How many children per generation
GENERATION_SIZE = 50

# How many generations is too much
MAX_NUMBER_OF_GENERATIONS = 1000000

# How is fitness evaluated?
# 
# options:
# levenshtein_fitness
# exact_character_match_fitness
# least_non_matching_characters_fitness
FITNESS_FUNCTION = fitness_functions.levenshtein_fitness

#
# LOOK INTO http://docs.python.org/2/library/difflib.html for fitness
#

# MUTATION PROBABILITIES
LETTER_CHANGE_CHANCE = 0.01
LETTER_DELETION_CHANCE = 0.01
INSERT_SPACE_CHANCE = 0.01

# Defines pool of characters from which random draws can be made
POSSIBLE_CHARACTERS = string.ascii_lowercase + '.,?:'