# Benchmark various serialization options for the hyphenate example.
# Outputs: input name, serialization format, runtime, 3-sigma uncertainty in runtime

import time, subprocess, os, random, statistics, math

N = 100

# yaml not included here because it's just so ridiculously slow that I know I wouldn't use it.
# You can add yaml, just give the script plenty of time to run.
subdirs = ["baseline", "json", "pickle", "msgpack", "yaml"]

inputs = [
	["empty", b"", b""],
	["short", b"oversimplification", b"over|sim|pli|fi|ca|tion\n"],
]

# Verify that inputs map to the correct outputs.
def check_call(subdir, input, expected):
	t0 = time.time()
	process = subprocess.Popen(["python3", "main.py"], cwd=subdir, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	output, errs = process.communicate(input)
	assert(output == expected and not errs)

# Set up each subdirectory and verify the inputs.
for subdir in subdirs:
	if os.path.exists(os.path.join(subdir, "make.py")):
		process = subprocess.Popen(["python3", "make.py"], cwd=subdir)
		process.communicate()
	for iname, input, expected in inputs:
		check_call(subdir, input, expected)

# Determine the time for a single invocation for the given subdirectory.
def time_call(subdir, input, expected):
	t0 = time.time()
	process = subprocess.Popen(["python3", "main.py"], cwd=subdir, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL)
	process.communicate(input)
	return time.time() - t0

for iname, input, expected in inputs:
	# We want to do N trials for each serialization format, in a random order for debiasing.
	trials = subdirs * N
	random.shuffle(trials)
	times = { subdir: [] for subdir in subdirs }
	for subdir in trials:
		times[subdir].append(time_call(subdir, input, expected))
	output = [iname]
	for subdir in subdirs:
		mu = statistics.mean(times[subdir])
		sigma = statistics.stdev(times[subdir])
		uncertainty = 3 * sigma / math.sqrt(N)
#		print(f"{iname}\t{subdir}\t{mu:.4f}\t{uncertainty:.2f}")
		print("{}\t{}\t{:.6f}\t{:.6f}".format(iname, subdir, mu, uncertainty))

