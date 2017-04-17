import pickle, os.path, sys

data_directory = "data"
pickle_file = os.path.join(data_directory, "hyphenate.pkl")
hyphenator = pickle.load(open(pickle_file, "rb"))

for line in sys.stdin:
	print(" ".join(hyphenator.hyphenate_word(word) for word in line.split()))

