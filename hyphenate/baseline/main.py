import os.path, sys
import hyphenate

data_directory = "data"

patterns = open(os.path.join(data_directory, "patterns.txt")).read().split()
exceptions = open(os.path.join(data_directory, "exceptions.txt")).read().split()

hyphenator = hyphenate.Hyphenator(patterns, exceptions)

for line in sys.stdin:
	print(" ".join(hyphenator.hyphenate_word(word) for word in line.split()))

