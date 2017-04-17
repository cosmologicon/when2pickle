import pickle, os.path
import hyphenate

data_directory = "data"
pickle_file = os.path.join(data_directory, "hyphenate.pkl")

patterns = open(os.path.join(data_directory, "patterns.txt")).read().split()
exceptions = open(os.path.join(data_directory, "exceptions.txt")).read().split()
hyphenator = hyphenate.Hyphenator(patterns, exceptions)
pickle.dump(hyphenator, open(pickle_file, "wb"))

