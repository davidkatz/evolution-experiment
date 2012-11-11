import evolutiontools

# ----------------------
# TEST ROLL_WEIGHTED DIE
# ----------------------

print ''
print 'ROLL_WEIGHTED_DIE'
print '-----------------'
print ''

NUMBER_OF_TEST_THROWS = 1e5 # a hundred thousand

# define die events and their string constants

letter_change = 'LETTER_CHANGE'
letter_deletion = 'LETTER_DELETION'
letter_duplication = 'LETTER_DUPLICATION'

# set up counters to store die throw results

change_counter = 0;
deletion_counter = 0;
duplication_counter = 0;

# throw the dice many times, store results 

for num in range(0,int(NUMBER_OF_TEST_THROWS)):
	result = evolutiontools.roll_weighted_die({
		'LETTER CHANGE': 0.05,
		'LETTER DELETION': 0.02,
		'LETTER DUPLICATION': 0.02
		})
	if result == 'LETTER CHANGE':
		change_counter += 1
	if result == 'LETTER DELETION':
		deletion_counter += 1
	if result == 'LETTER DUPLICATION':
		duplication_counter += 1

# check if results are around the expected values
print 'CHANGE: ' + str(change_counter/NUMBER_OF_TEST_THROWS)
print 'DELETION: ' + str(deletion_counter/NUMBER_OF_TEST_THROWS)
print 'DUPLICATION: ' + str(duplication_counter/NUMBER_OF_TEST_THROWS)


# --------------------
# TEST COPY AND MUTATE
# --------------------

print ''
print 'COPY_AND_MUTATE'
print '---------------'
print ''

for num in range (1,10):
	print ''.join(evolutiontools.copy_and_mutate("1234567890"))
	print ''


# ------------------------
# TEST SURVIVE_SELECTIVELY
# ------------------------

print '-------------------'
print 'SURVIVE SELECTIVELY'
print '-------------------'
print ''

a = list('whaddup?')
b = list('hello nurse')
c = list('hello work')

test_generation = [a,b,c]
print ''.join(evolutiontools.survive_selectively(test_generation,'hello world'))


# ------------------
# TEST MAKE_CHILDREN
# ------------------
print ''
print '-------------'
print 'MAKE_CHILDREN'
print '-------------'
print ''

father = 'how tall are you?'
children = evolutiontools.make_children(father,10)
for child in children:
	print ''.join(child)

