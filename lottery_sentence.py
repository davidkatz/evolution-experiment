import string, os, random, sys, evolution_tools

GOAL_ORGANISM = sys.argv[1] # What we're trying to evolve
possible_characters = string.ascii_lowercase + '.,?:'
MAX_NUMBER_OF_TRIES = 10000000 # ten million


for num in range(0,MAX_NUMBER_OF_TRIES):
	random_string = evolution_tools.get_random_string(2*len(GOAL_ORGANISM))
	print str(num) + ': ' + random_string
	if random_string == GOAL_ORGANISM:
		print 'GOAL REACHED'
		print 'ORGANISMS SAMPLED: ' + str(num)
		break