import json, os.path, sys
import hyphenate

data_directory = "data"
json_file = os.path.join(data_directory, "hyphenate.json")

hyphenator = hyphenate.Hyphenator([], [])
tree, exceptions = json.load(open(json_file, "r", encoding="utf-8"))

# JSONifying a Python dict converts None keys into the string "null".
# Convert them back to Nones before using.
# If you don't include this step, hyphenation will fail silently and give a wrong result.
def none_keys(d):
	if u"null" in d:
		d[None] = d[u"null"]
		del d[u"null"]
	for v in d.values():
		if isinstance(v, dict):
			none_keys(v)

none_keys(tree)
hyphenator.tree = tree
hyphenator.exceptions = exceptions

for line in sys.stdin:
	print(" ".join(hyphenator.hyphenate_word(word) for word in line.split()))

