import urllib

story = urllib.urlopen('https://sixty-north.com/c/t.txt')
story_words = []
for line in story:
	line_words = line.split()
	for word in line_words:
		story_words.append(word)
story.close()

for word in story_words:
	print(word)


