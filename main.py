from trie.trie import Trie
from trie.suggestlist import Suggestlist
import timeit

# Load words and queries in Trie
trie = Trie()
trie.addWords('/home/martijn/git/_py_playground/words.xml', 'topKeyword', 'keyword')
trie.addWords('/home/martijn/git/_py_playground/queries.xml', 'topQuery', 'query')

# Add words to array
suggestlist = Suggestlist()
suggestlist.addWords('/home/martijn/git/_py_playground/words.xml', 'topKeyword', 'keyword')
suggestlist.addWords('/home/martijn/git/_py_playground/queries.xml', 'topQuery', 'query')


prefixes = ['pi', 'go', 'kp', 'kla', 'opze', 'showc']

# List
for prefix in prefixes:
    suggestlist.starts_with_prefix(prefix)


# Trie
start_time = timeit.default_timer()
for prefix in prefixes:
    words = trie.start_with_prefix(prefix)
    print 'Words and queries starting with '+prefix+':'
    print words

elapsed = timeit.default_timer() - start_time

print 'Took: '+str(elapsed)+' seconds'

