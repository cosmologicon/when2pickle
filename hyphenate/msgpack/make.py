import msgpack, os.path
import hyphenate

data_directory = "data"
msgpack_file = os.path.join(data_directory, "hyphenate.mpk")

patterns = open(os.path.join(data_directory, "patterns.txt")).read().split()
exceptions = open(os.path.join(data_directory, "exceptions.txt")).read().split()
hyphenator = hyphenate.Hyphenator(patterns, exceptions)

obj = hyphenator.tree, hyphenator.exceptions
data = msgpack.packb(obj)
open(msgpack_file, "wb").write(data)

