import json, os.path
import hyphenate

data_directory = "data"
json_file = os.path.join(data_directory, "hyphenate.json")

patterns = open(os.path.join(data_directory, "patterns.txt")).read().split()
exceptions = open(os.path.join(data_directory, "exceptions.txt")).read().split()
hyphenator = hyphenate.Hyphenator(patterns, exceptions)
obj = hyphenator.tree, hyphenator.exceptions
json.dump(obj, open(json_file, "w", encoding="utf-8"))

