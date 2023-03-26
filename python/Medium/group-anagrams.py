
# GROUP ANAGRAMS

def groupAnagrams(words):
    # Write your code here.
    anagrams = []
	anagramCounts = []
	for word in words:
		letterCount = returnCount(word)
		found = False
		for i, count in enumerate(anagramCounts):
			if count == letterCount:
				found = True
				anagrams[i].append(word)
				break
		if not found:
			anagramCounts.append(letterCount)
			anagrams.append([word])
			
	return anagrams

# O(N) time and space
def returnCount(word):
	count = {}
	for letter in word:
		if letter in count:
			count[letter] += 1
		else:
			count[letter] = 1
	return count


# O(Nlog(N) * w) time and O(w * N) space
def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
	for word in words:
		sortedWord = "".join(sorted(word))
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word)
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())
