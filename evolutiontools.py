import random, string

# simulates a rolling of a weighted die (as in dice). input is a dictionary 
# with possible results and their assigned probabilities, output is what result
# came up in a roll. if none of your results came up the output is 'None'
def roll_weighted_die(dice_dictionary):

	# this function works by picking a random float from 0 to 1
	# and mapping the result to the die's defined probabilities. say, 
	# if you want a die that returns 'black' with 0.2 chance and 'white' with
	# 0.4 chance - then the function gets a number from 0 to 1, and if it falls
	# between 0 and 0.2, it outputs 'black', if it falls from 0.2 to 0.6 it
	# outputs 'white', if it falls above 0.6 it outputs 'None' 

	chance_of_any_event = sum(dice_dictionary.values());

	if (chance_of_any_event > 1):
		raise ValueError("The sides of your die total to a higher probability than 1. That's impossible!")
	
	random_number = random.random() #returns a float from 0 to 1

	if random_number > chance_of_any_event:
		return None

	last = 0
	for key in dice_dictionary.keys():
		if last < random_number < last + dice_dictionary[key]:
			return key
		last += dice_dictionary[key]


# takes an organism and returns a copy that may be mutated
def copy_and_mutate(organism):
	
	# first, make a copy
	new_organism = list(organism); 

	# to start the mutation action, define events and their string constants
	letter_change = 'LETTER_CHANGE'
	letter_deletion = 'LETTER_DELETION'
	letter_duplication = 'LETTER_DUPLICATION'

	# define probabilities for mutation events 
	event_probabilities = {
		letter_change: 0.01,
		letter_deletion: 0.005,
		letter_duplication: 0.005
	}

	# iterate over the organism, allow mutations to happen
	for i,c in enumerate(new_organism):
		event = roll_weighted_die(event_probabilities)

		if event == letter_change:
			#print letter_change
			new_organism[i] = random.choice(string.ascii_lowercase)

		if event == letter_duplication:
			#print letter_duplication
			new_organism.insert(i,new_organism[i])

		if event == letter_deletion:
			#print letter_deletion
			del new_organism[i]
	    
	return new_organism


def make_children(father, generation_size):
	children=list()
	for num in range(0,generation_size):
		children.append(copy_and_mutate(father))
	return children


# Calculates the levenshtein distance between a and b. Lower levenshtein
# distances means more similar strings, with a score of 0 meaning an identical
# string. (taken from http://hetland.org/coding/python/levenshtein.py)
def levenshtein(a,b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n
        
    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
            
    return current[n]


# this is a small helper function. our survival function is going to be based on
# levenshtein distances, where levenshtein(a,b). we want to define 
# string similarity as 'fitness'. for elegance though, we want higher fitness to mean 
# survival, not lower fitness. this function inverts a levenshtein distance to give us
# a number that approaches 1 as strings become more similar
def levenshtein_fitness(a,b):
	return 1.0/(1.0+levenshtein(a,b))


# takes a generation of organisms as input, returns one survivor. an organisms
# fitness is derived from the levenshtein distance between itself and the ideal_organism
def survive_selectively(generation, ideal_organism):
	best_fitness = 0
	for child in generation:
		child_fitness = levenshtein_fitness(child,ideal_organism)
		if child_fitness > best_fitness:
			survivor = child
			best_fitness = child_fitness
	return survivor


