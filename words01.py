from time import sleep
from progress.bar import Bar
from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)

print(story_words)

bar = Bar('Loading bla bla', fill='>', suffix='%(percent)d%%')
bar.max = 50

rowsCounter = 0
print("Starting to load data... ")

for row in range(50):
    sleep(0.08)

    # Increment counter
    rowsCounter += 1
    bar.index = rowsCounter
    bar.next()
