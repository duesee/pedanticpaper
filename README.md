# Pedanticpaper

This script spots several mistakes in TeX files, a spell-checker won't. In order to work, a configuration file must be defined.

Currently, the tool does the following:

* Find "evil twins", e.g. check that "side-channel" was always used instead of "side channel" or "sidechannel".
* Check for consistency of section-, subsection-, etc. title, e.g. "How to write Research Papers" (upper-case style) vs. "How to write research papers" (lower-case style). The implementation must be provided in the config file.
* Warn on potentially confusing words like "proposed" and "purposed".
* Find doublettes, i.e. "We showed that that..."
* Find non-allowed characters, i.e. difficult to spot unicode characters which may introduce parsing errors.

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
$ python main.py                                                       130 ↵
### Testing file test/classic.tex
[!] found non-allowed char '²' in line 3
[!] found bad twin "elliptic-curve" in line 3. Did you mean "elliptic curve"?
[!] found doublette ('the', 'the') in line 3

### Testing file test/input/ecc.tex
[!] found bad twin "public-key" in line 3. Did you mean "public key"?
[?] found potentially confusing word "purposed" in line 3. Did you mean "proposed"?
[!] found doublette ('is', 'is') in line 3
```

# Important

The script may contain "unpythonic" or unelegant code and insult pedantic programmers. Beside from that,
it does not change any files and pull-request are welcome.
