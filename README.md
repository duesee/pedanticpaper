# Pedanticpaper

The script at hand finds several mistakes when writing research papers, a spell-checker won't. This is archieved by defining a per-project configuration file.

Currently, the tool does the following:

* It checks for "evil twins", i.e. that a single notation (e.g. "side-channel") was used instead of different ones (e.g. "side channel" or "sidechannel"). This is especially useful when content is provided by multiple authors.
* It finds doublettes, i.e. "We showed that that...". This can happen due to copy-paste errors and can easily be overlooked.
* It finds non-allowed characters, i.e. difficult to spot unicode characters which may introduce parsing errors.
* It checks for consistency in titles, i.e. if the same style (e.g. upper-case style "How to write a Research Paper" or lower-case style "How to write a research paper") is used to name each section, subsection, etc.
* It warns on potentially confusing words like "proposed" and "purposed".

# Sample Configuration

```Python
import string

config = {
    "allowed_chars": string.printable + "ÄÖÜäöüß",
    "notation_levels": {
        "ignore_words": [
            "of", "on", "the", "to", "for",
            "and", "with", "without", "any"
        ],
        "section": check_notation_section,
        "subsection": check_notation_subsection,
        "subsubsection": check_notation_subsubsection,
        "paragraph": check_notation_paragraph,
        "subparagraph": check_notation_subparagraph,
    },
    "notation_twins": [
        ("public key", ["public-key", "publickey", "pubkey"]),
        ("elliptic curve", ["elliptic-curve"])
    ],
    "confusing_words": [
        ("threat", ["thread"]),
        ("proposed", ["purposed"])
    ],
    "checks": [
        "check_allowed_chars",
        "check_notation_levels",
        "check_twins",
        "check_confusing",
        "check_doubled_words",
    ]
}
```

# Sample

```
$ python main.py ./
### Starting recursive search from "./"
### Testing file "classic.tex"
[!] found non-allowed char '²' in line 3
[!] found evil twin "elliptic-curve" in line 3. Did you mean "elliptic curve"?
[!] found doublette "the the" in line 3

### Testing file "ecc.tex"
[!] found evil twin "public-key" in line 3. Did you mean "public key"?
[?] found potentially confusing word "purposed" in line 3. Did you mean "proposed"?
[!] found doublette "is is" in line 3
```

# Important

The script may contain "unpythonic" or unelegant code and insult pedantic programmers. Beside from that, it does not change any files and pull-request are always welcome.
