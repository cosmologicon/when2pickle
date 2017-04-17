import yaml, os.path
import hyphenate

data_directory = "data"
yaml_file = os.path.join(data_directory, "hyphenate.yaml")

patterns = open(os.path.join(data_directory, "patterns.txt")).read().split()
exceptions = open(os.path.join(data_directory, "exceptions.txt")).read().split()
hyphenator = hyphenate.Hyphenator(patterns, exceptions)
obj = hyphenator.tree, hyphenator.exceptions
obj = hyphenator
yaml.dump(obj, open(yaml_file, "w", encoding="utf-8"))

