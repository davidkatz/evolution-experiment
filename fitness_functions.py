import evolution_math
import string
import time

# -------------------------
# VARIOUS FITNESS FUNCTIONS
# -------------------------

# this defines fitness as the number of exact matching characters
# in two strings. for example, 'hello' and 'help' have a score of 3.
# 'india' and 'london' have a score of 0
def exact_character_match_fitness(a,b):

	fitness = 0;
	for i in range(0,min(len(a),len(b))):
		if a[i] == b[i]:
			fitness += 1
	return fitness


# 
def least_non_matching_characters_fitness(a,b):
    if len(a) < len(b):
        shorter_list = a
    else:
        shorter_list = b

    nonmatches = 0

    for i in range(0,len(shorter_list)):
        if a[i] != b[i]:
            nonmatches += 1

    nonmatches += abs(len(a)-len(b))
    fitness = 1.0/(1.0+nonmatches)
    return fitness

    
# this is a small helper function. our survival function is going to be based on
# levenshtein distances, where levenshtein(a,b). we want to define 
# string similarity as 'fitness'. for elegance though, we want higher fitness to mean 
# survival, not lower fitness. this function inverts a levenshtein distance to give us
# a number that approaches 1 as strings become more similar
def levenshtein_fitness(a,b):
	return 1.0/(1.0+evolution_math.levenshtein(a,b))