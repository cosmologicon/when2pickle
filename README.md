# when2pickle
Demonstration of a good usage of the Python pickle module

# Introduction

[The Python `pickle` module](https://docs.python.org/3.6/library/pickle.html) lets you serialize
arbitrary Python objects to disk. It comes with two important caveats:

1. The `pickle` module is not secure against erroneous or maliciously constructed data. Never
unpickle data received from an untrusted or unauthenticated source.
1. Pickled objects are not guaranteed to be usable if you change your source code, for instance if
you release an update. (This is actually true of all serialization formats, but some of them make it
easier to deal with than others.)

Please make sure you understand these two caveats. I completely agree with them.

Having said that, some people think these caveats mean you should never use `pickle`, and there I
disagree. Yes `pickle` can be misused, but that doesn't mean it's impossible or even all that hard
to use it well. If you think that it's not worth putting any thought into the tool you use, you
should just avoid `pickle` at all costs to make sure you're not misusing it, then keep in mind that
`pickle` has two big advantages over other serialization options in Python:

1. It's fast.
1. It requires you to write less custom serialization code. Less code means less chances for errors.
Thus `pickle`, when used correctly, is less error-prone than other options used correctly.

Therefore I claim that if you're writing a Python program that requires some non-trivial state,
that can be reconstructed if needed, and you care about speed or about avoiding bugs, then `pickle`
is a good tool to consider.

This repository contains examples of problems where I think it's appropriate to use `pickle`. For
each problem, I implement several different solutions using different serialization modules. I'll
measure runtime benchmarks, as well as give my subjective opinion on the additional code overhead
required to use different solutions.

# Example: hyphenation

## Problem description

Write a Python script that adds hyphenation breaks to English text, so that you know where you can
break a word for hyphenation. Use the algorithm created by Frank Liang, for which there is a [Python
implementation by Ned Batchelder](https://nedbatchelder.com/code/modules/hyphenate.html).

## Serialization formats evaluated

1. No serialization (baseline)
1. `json`
2. `pickle`
3. `msgpack`
4. `yaml`

## Verdict

For this problem, serialization is probably not crucial. The baseline implemetation without
serialization already runs fairly fast. You can probably get away without serialization here, unless
you care a lot about speed.

![Hyphenation runtimes](/imgs/hyphenation-results?raw=true "Runtime for each of the serialization options in the hyphenation example")

| format | runtime (s) | uncertainty (s) |
| ------ | ----------- | --------------- |
| baseline | 0.0670 | 0.00083 |
| json | 0.0556 | 0.00085 |
| pickle | 0.0459 | 0.00174 |
| msgpack | 0.0583 | 0.00059 |
| yaml | 4.2091 | 0.04437 |

However, if you do care about speed and decide to serialize, `pickle` is the clear winner. It's the
fastest option, about 32% faster than baseline, and requires zero additional code. `json` and
`msgpack`, in addition to being slower (17% and 13% slower than baseline), both require tweaking the
internals of the `hyphenate` object. It's not a lot of additional code, but it's sort of ugly. I had
to use `isinstance` to check the types in the deserialized data.

Furthermore, both `json` and `msgpack` failed silently before I added this tweak. It acted as if it
had run correctly, but no hyphenation breaks were actually added. Of course you should always test
your code, but be extra vigilant if you're serializing Python objects with `json` or `msgpack`.

`yaml`, like `pickle`, requires no additional code, but it's completely unusable here, being far too
slow, around 100x slower than other options.

`msgpack` has the smallest file size, but still larger than baseline.
