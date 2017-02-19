# Define allowed characters

Detect characters, e.g. unicode chars, which may introduce subtle errors in TeX files.
We find the following definition suitable for german texts, e.g.

```Python
"allowed_chars": string.printable + "ÄÖÜäöüß",
```

# Detect evil twins

Define the correct notation for specific words. The first element in the tuple denotes the correct version,
the second is a lists of various "evil twins", e.g.

"""Python
"evil_twins": [
    ("public key", [r"(public\-*key[^s])"]),
    ("public keys", [r"(public\-*keys)"]),
    ("elliptic curve", [r"(elliptic\s*\-+\s*curve[^s])"]),
    ("elliptic curves", [r"(elliptic\s*\-+\s*curves)"])
],
"""

# Wrong abbreviations

The same `(good, [err1, err2, ...])` pattern applies as in evil twins, e.g.

"""Python
"wrong_abbrev": [
    ("et al.", ["(et\.*\s*al\.*)"]),
    ("i.e.", [r"\W(i\s*\.*\s*e\.*)\W"]),
    ("e.g.", [r"\W(e\s*\.*\s*g\.*)\W"]),
    ("etc.", [r"(etc\.*)"])
],
"""

# Potentially confusing words

Some words pass a spell-check, but may carry very different meaning. If you spot some of them
during writing, put them here to be prepared in the future. The first part of the tuple is the
"probably right" word -- use `None` if there is none.

"""Python
"confusing_words": [
    ("threat", ["thread"]),
    ("proposed", ["purposed"]),
    (None, ["leek", "lack", "leak"]),
],
"""

# Leftovers in text such as TODO, TBD, etc.

Make sure there are no leftovers. Matching is done case-insensitive.

"""Python
"denied_words": load_csv("assets/denied_words.csv"),
"""

# Weasel words

"A weasel word (...) is an informal term for words and phrases aimed at creating an
impression that a specific or meaningful statement has been made, when instead only
a vague or ambiguous claim has actually been communicated." (https://en.wikipedia.org/wiki/Weasel_word)

"""Python
"weasel_words": load_csv("assets/weasel_words.csv"),
"""

# Passive voice

"The passive voice is a grammatical construction (specifically, a "voice"). The noun or noun phrase that
would be the object of an active sentence (such as Our troops defeated the enemy) appears as the subject
of a sentence or clause in the passive voice (e.g. The enemy was defeated by our troops)."
(https://en.wikipedia.org/wiki/English_passive_voice)

"""Python
"passive_voice": load_csv("assets/passive_voice.csv"),
"""

# Thanks

Some of the list were taken from http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/. Thanks!