# Pedanticpaper

The script at hand finds several mistakes when writing research papers, a spell-checker won't. This is archieved by defining a per-project configuration file.

Currently, the tool does the following:

* It checks for "evil twins", i.e. that a single notation (e.g. "side-channel") was used instead of different ones (e.g. "side channel" or "sidechannel"). This is especially useful when content is provided by multiple authors.
* It finds doublettes, i.e. "We showed that that...". This can happen due to copy-paste errors and can easily be overlooked.
* It finds non-allowed characters, i.e. difficult to spot unicode characters which may introduce parsing errors.
* It checks for consistency in titles, i.e. if the same style (e.g. upper-case style "How to write a Research Paper" or lower-case style "How to write a research paper") is used to name each section, subsection, etc.
* It warns on potentially confusing words like "proposed" and "purposed".
* It checks for wrong abbreviation, e.g. "et al" or "ie.".
* It checks for so called ["weasel words"](https://en.wikipedia.org/wiki/Weasel_word).

# Sample Configuration

```Python
import string
import json


def load_json(path):
    return json.load(open(path, "rt"))


config = {
    "regex_doublettes": r"(\w+)\b\s+(\1)\b",
    "allowed_chars": string.printable + "ÄÖÜäöüß",
    "evil_twins": load_json("assets/evil_twins.json"),
    "wrong_abbrev": load_json("assets/wrong_abbrev.json"),
    "confusing_words": load_json("assets/confusing_words.json"),
    "denied_words": load_json("assets/denied_words.json"),
    "weasel_words": load_json("assets/weasel_words.json"),
    "passive_voice": load_json("assets/passive_voice.json"),
    "checks": [
        "check_allowed_chars",
        "check_doubled_words",
        "check_evil_twins",
        "check_abbrev",
        "check_weasel_words",
        "check_passive_voice",
        "check_denied_words",
        "check_confusing",
    ]
}
```

# Sample

```
$ python main.py ./
Starting recursive search from "./"
File "classic.tex:"
	Line 7: found doublette "the the".
	Line 7: found non-allowed char '²'.
	Line 8: found evil twin "elliptic-curves". Did you mean "elliptic curves"?
	Line 9: found erroneous abbreviation "e.g ". Did you mean "e.g."?
	Line 9: found erroneous abbreviation "eg.". Did you mean "e.g."?

File "ecc.tex:"
	Line 3: found potentially confusing word "purposed". Did you mean "proposed"?
	Line 5: found doublette "is is".
	Line 6: found doublette "and and".
	Line 9: found denied word "todo". Please resolve it.
	Line 9: found weasel word "extremely". Can it be clarified?
```

# Help building regular expressions

See [regex101](https://regex101.com/).

# Important

The script at hand may contain unpythonic and/or unelegant code and insult pedantic programmers. Beside from that, it does not change any files and pull-request are always welcome.
