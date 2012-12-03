import os, random, string
import fitness_functions, config

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
def copy_and_mutate_levenshtein_friendly(organism):

	# first, make a copy
	new_organism = list(organism); 

	# to start the mutation action, define events and their string constants
	letter_insert = 'LETTER_INSERT'
	letter_delete = 'LETTER_DELETE'
	letter_change = 'LETTER_CHANGE'

	# define probabilities for mutation events 
	event_probabilities = {
		letter_insert: 0.15,
		letter_delete: 0.15,
		letter_change: 0.1
	}

	event = roll_weighted_die(event_probabilities)
	change_site = random.randint(0,len(organism)-1)

	if event == letter_change:
		
		new_organism[change_site] = random.choice(config.POSSIBLE_CHARACTERS)

	if event == letter_delete:
		
		del new_organism[change_site]

	if event == letter_insert:
		
		new_organism.insert(change_site,random.choice(config.POSSIBLE_CHARACTERS))
	return new_organism	
	
# takes an organism and returns a copy that may be mutated
def copy_and_mutate(organism):

	# first, make a copy
	new_organism = list(organism); 

	# to start the mutation action, define events and their string constants
	letter_change = 'LETTER_CHANGE'
	letter_deletion = 'LETTER_DELETION'
	insert_space = 'INSERT_SPACE'

	# define probabilities for mutation events 
	event_probabilities = {
		letter_change: config.LETTER_CHANGE_CHANCE,
		letter_deletion: config.LETTER_DELETION_CHANCE,
		insert_space: config.INSERT_SPACE_CHANCE
	}

	# iterate over the organism, allow mutations to happen
	for i,c in enumerate(new_organism):
		event = roll_weighted_die(event_probabilities)

		if event == letter_change:
			#print event
			new_organism[i] = random.choice(config.POSSIBLE_CHARACTERS)

		if event == insert_space:
			#print event
			new_organism.insert(i,' ')

		if event == letter_deletion:
			#print event
			del new_organism[i]
	return new_organism


def make_children(father, generation_size):
	children=list()
	for num in range(0,generation_size):
		children.append(copy_and_mutate(father))
	return children


# takes a generation of organisms as input, returns one survivor. an organisms
# fitness is derived from the levenshtein distance between itself and the ideal_organism
def survive_selectively(generation, ideal_organism):
	best_fitness = 0
	for child in generation:
		child_fitness = config.FITNESS_FUNCTION(child,ideal_organism)
		if child_fitness >= best_fitness:
			survivor = child
			best_fitness = child_fitness
	return survivor

def get_random_string(max_length):
    random_string_length = random.randint(1,max_length)
    return ''.join(random.choice(config.POSSIBLE_CHARACTERS) for x in range(random_string_length))