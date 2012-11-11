import random, os, string
import evolutiontools

# SETTINGS

GOAL_ORGANISM = 'whatdoyouknowsherlock'  # What we're trying to evolve
GENERATION_SIZE = 10            # How many children per generation

# Ok, here we go

# seed a random string
# random_string_length = random.randint(0,2*len(GOAL_ORGANISM))
# random_string = os.urandom(random_string_length)

# gotta start somewhere
survivor = list('dlf!#@$!9')
best_fitness = 0

for num in range(0,100000):
    children = evolutiontools.make_children(survivor,10)
    survivor = evolutiontools.survive_selectively(children,GOAL_ORGANISM)
    print ''.join(survivor)
    if ''.join(survivor) == GOAL_ORGANISM:
        print 'GOAL REACHED!'
        break

if ''.join(survivor) != GOAL_ORGANISM:
    print "DIDN'T WORK"

