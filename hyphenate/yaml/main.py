import yaml, os.path, sys
import hyphenate

data_directory = "data"
yaml_file = os.path.join(data_directory, "hyphenate.yaml")
hyphenator = yaml.load(open(yaml_file, "r", encoding="utf-8"))
for line in sys.stdin:
	print(" ".join(hyphenator.hyphenate_word(word) for word in line.split()))

