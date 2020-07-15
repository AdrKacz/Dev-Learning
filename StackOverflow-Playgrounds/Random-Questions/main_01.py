def FindDifference(word):
	letters = list("programmer")

	i = 0
	j = 0
	while i < len(word) and j < len(letters):
		if word[i] == letters[j]:
			j+=1
		i+=1
	start = i - 1

	if i == len(word):
		return -1

	i = len(word)
	j = len(letters)
	while i > 0 and j > 0:
		i -= 1
		if word[i] == letters[j - 1]:
			j-=1
	end = i

	return end - start - 1

if __name__ == '__main__':
	print(FindDifference("progxrammerrxproxgrammer"))