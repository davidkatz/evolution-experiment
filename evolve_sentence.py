import random, os, string, sys
import evolution_tools, evolution_math, config

# SETTINGS

GOAL_ORGANISM = list(sys.argv[1])  # What we're trying to evolve

# Ok, here we go

# seed a random string
# random_string_length = random.randint(0,2*len(GOAL_ORGANISM))
# random_string = os.urandom(random_string_length)

# gotta start somewhere
survivor = list(evolution_tools.get_random_string(2*len(GOAL_ORGANISM)))

for num in range(0,config.MAX_NUMBER_OF_GENERATIONS):
    children = evolution_tools.make_children(survivor,config.GENERATION_SIZE)
    survivor = evolution_tools.survive_selectively(children,GOAL_ORGANISM)
    print str(num*config.GENERATION_SIZE) + ': ' + ''.join(survivor)
    if ''.join(survivor) == ''.join(GOAL_ORGANISM):
        print 'GOAL REACHED!'
        print 'ORGANISMS SAMPLED: ' + str(num*config.GENERATION_SIZE)
        break

if ''.join(survivor) != GOAL_ORGANISM:
    print "DIDN'T WORK"