import msgpack, os.path, sys
import hyphenate

data_directory = "data"
msgpack_file = os.path.join(data_directory, "hyphenate.mpk")

data = open(msgpack_file, "rb").read()
tree, exceptions = msgpack.unpackb(data)

# MessagePack in Python dict converts str keys into bytes.
# Convert them back to str before using.
# If you don't include this step, hyphenation will fail silently and give a wrong result.
def str_keys(d):
	for k, v in list(d.items()):
		if isinstance(k, bytes):
			d[k.decode("utf-8")] = d[k]
			del d[k]
		if isinstance(v, dict):
			str_keys(v)
str_keys(tree)

hyphenator = hyphenate.Hyphenator([], [])
hyphenator.tree = tree
hyphenator.exception = exceptions

for line in sys.stdin:
	print(" ".join(hyphenator.hyphenate_word(word) for word in line.split()))

