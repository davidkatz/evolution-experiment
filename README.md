# Evolution Experiments

At this stage, this is a pure 'messing around' side project. My first goal is to write an environment in which sentences like *Hello World* can evolve from any other sentence or collection of characters. 

The desired process is modelled after evolution as best as I could muster. It starts from any set of characters (say, '324X!#$'), and then goes through a gradual process of:

* making children (read: copy and mutate), and
* selectively "surviving" those children (read: measure them against a fitness function which makes only the most fit child survive).

This is repeated ad-infinitum until your goal sentence is reached.

Right now, this project supports three kind of mutations to sentences, each one of which can occur at a defined probability.

* Random Letter Change (where, say 'a' turns into 'x')
* Letter Duplication ('a' -> 'aa')
* Letter Deletion ('a' -> '')

Each sentence's "fitness" is derived from the Levenshtein distance between itself and the goal sentence. (http://en.wikipedia.org/wiki/Levenshtein_distance)

Right now evolving phrases without spaces works great (things like 'helloworldhowareyoutoday').  

NOTE: there's nothing 'useful' for you here. Your only conceivable reason for grabbing this code is if you want to go through it's guts and play. If that's your bag - by all means, fork away and submit pull requests. 