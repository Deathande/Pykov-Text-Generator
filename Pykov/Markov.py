import random
import re

# G3nerate the relations between words in the given text.
# Returns a dictionary representing the word relations,
# and a list containing all the words
def gen_relation(text):
	relations = {}
	words = re.split('\s+', text)

	# Because the above split will append some empty strings
	# we will remove them here. With a more robust regular
	# expression this will not be necessary.
	while(words.count('')):
		words.remove('')
	for i in range(len(words) - 1):
		if words[i] in relations:
			relations[words[i]].append(words[i+1])
		else:
			relations[words[i]] = [words[i+1]]
	return relations

# Generate a string via markov chains based on the given
# text. Generates num words and a relations dictionary can
# be provided so it does not have to regenerate one.
def gen_with_text(text, num):
	relations = gen_relation(text)
	return gen_with_relations(relations, num)

def gen_with_relations(relations, num):
	words = list(relations.keys())
	words = [words[random.randint(0, len(words)-1)]]
	for i in range(num-1):
		if not words[-1] in relations:
			current_sentence = " ".join(words)
			next_part = current_sentence + " " + gen_with_relations(relations, num - i)
			return next_part
		arr = relations[words[-1]]
		n_word = arr[random.randint(0, len(arr)-1)]
		words.append(n_word)
	return " ".join(words)

if __name__ == '__main__':
	txt = "SW.txt"
	f = open(txt, 'r')
	print(gen(f.read(), 20))
