## Pedanticpaper

The script at hand finds mistakes when writing research papers, a spell-checker won't. This is archieved by defining a per-project configuration file.

Currently, the tool does the following:

* It checks for "evil twins", i.e. that a single notation (e.g. "side-channel") and not different ones (e.g. "side channel" or "sidechannel") were used. This is especially useful when content is provided by multiple authors.
* It finds doubletes, i.e. "We showed that that...". This can happen due to copy-paste errors and is easily overlooked.
* It finds non-allowed characters, i.e. difficult to spot unicode characters which may introduce parsing errors.
* It warns on potentially confusing words like "proposed" and "purposed", which pass a spell-check, but carry different meaning. If you spot some of them during writing, put them in the config-file to be prepared in the future.
* It checks for wrong abbreviation like "et. al" or "ie.".
* It checks for so called "weasel words" and passive voice. See [shell-scripts-for-passive-voice-weasel-words-duplicates](http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/).


### Sample.

```
$ python main.py "./"
Starting recursive search from "./"
File "test/classic.tex:"
	Line 7: found doublet "the the".
	Line 7: found non-allowed char '²'.
	Line 8: found evil twin "elliptic-curves". Did you mean "elliptic curves"?
	Line 9: found erroneous abbreviation "e.g ". Did you mean "e.g."?

File "test/input/ecc.tex:"
	Line 3: found potentially confusing word "purposed". Did you mean "proposed"?
	Line 6: found doublet "and and".
	Line 9: found probably leftover word "todo". Please resolve it.
	Line 9: found weasel word "extremely". Can it be clarified?
	Line 10: found evil twin "rsa". Did you mean "RSA"?
```

### Configuration.

```Python
config = {
    "regex_doublets": r"\b(\w+)\b\s+\b(\1)\b",
    "allowed_chars": string.printable + "ÄÖÜäöüß",
    "evil_twins": [
        (False, "public key", ["public-key"]),
        (True,  "RSA",        ["rsa", "Rsa"])
    ],
    "wrong_abbrev": [
        (False, "et al.", [r"(et\.\s*al\.*|et\s+al[^\.])"]),
        (False, "i.e.",   [r"(i\.e[^\.]|ie\.|i\.\s+e\.)"]),
        (False, "e.g.",   [r"(e\.g[^\.]|eg\.|e\.\s+g\.)"])
    ],
    "confusing_words": [
        (False, "threat", ["thread"]),
        (False, None,     ["lack", "leak", "lacks", "leaks"])
    ],
    "leftover_words": [
        "todo",
        "unfinished"
    ],
    "weasel_words": [
        "many",
        "completely"
    ],
    "passive_voice": [
        "awoken",
        "written"
    ],
    "checks": [
        "check_allowed_chars",
        "check_doubled_words",
        "check_abbrev",
        "check_evil_twins",
        "check_weasel_words",
        "check_passive_voice",
        "check_leftover_words",
        "check_confusing",
    ]
}
```

### Configuration format.

The format for evil twins, abbrev., etc. is as follows:

```python
(case_sensitive, correct_version, [incorrect_version, incorrect_version, ...])
```

The tool automatically includes word-boundaries if a "simple word", i.e. a string without a backslash, is provided. The code is as follows:

```python
if "\\" in word: word = r"\b({})\b".format(word)
```

This is so that `"is"` will not match against `"Th(is) is an example..."` and authors must not write `r"\\b(is)\\b"`. Otherwise, the original string is used as regex. The second element in the tuple is the "probably right" word -- use `None` if there is none. (This only applies to `confusing_words`).

### Help building regular expressions.

See [regex101](https://regex101.com/).

### Thanks.

The weasel- and passive voice lists were taken from http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/.

### Important.

The script at hand may contain unpythonic and/or unelegant code and insult pedantic programmers. Beside from that, it does not change any files and pull-request are always welcome.
