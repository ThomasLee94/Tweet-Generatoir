# * What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
- My sample.py prints the most likely word based on a given histogram of word: frequency key value pair.

# * Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
- I think so! I've made it as modular as I can with reasonable abstraction.

# * What are the scopes of variables and are they appropriate for their use case? If there are global variables, why are they needed?
- All variables are created and returned in their respective functions, no global variables were used.

# * Are the functions small and clearly specified, with as few side effects as possible?
- To the best of my ability, yes. Each of my functions do one task and return one 'thing'.

# * Are there functions that could be better organized in an Object-Oriented Programming style by defining them as methods of a class?
- There could be a histogram class, since it is something that is used quite often.

# * Can files be used as both modules and as scripts?
- Yes (modules are libraries you import/export and scripts are lines of code that are executed)

# * Do modules all depend on each other or can they be used independently?
- They can be used independently. 