# Autosuggest
Some autosuggest experiments with python. (Without any python experience)

## Trie
First is a test of a simple Trie implementation found here: https://nickstanisha.github.io/2015/11/21/a-good-trie-implementation-in-python.html
Slightly modified by adding weights to words for importance.

### data into trie
Trie.addWords() takes an XML file with similar structure like this:
```
<keywords>
   <keyword word="test">19</topKeyword>
   <keyword word="something">2</topKeyword>
</keywords>
```
Where 19 and 2 are the weights of the words.