import string


def check_notation_section(title):
    return True # To be done


def check_notation_subsection(title):
    return True # To be done


def check_notation_subsubsection(title):
    return True # To be done


def check_notation_paragraph(title):
    return True # To be done


def check_notation_subparagraph(title):
    return True # To be done


config = {
    # Detect characters, e.g. unicode chars, which may introduce subtle errors
    # in TeX files. We find the given definition suitable for german texts, but
    # use what you like.
    "allowed_chars": string.printable + "ÄÖÜäöüß",
    # Define the notation for section, subsection, etc. titles, e.g. upper-
    # "My Research Paper" vs lower-case "My research paper". The function
    # bodies at the top of this `config.py` can be defined to fulfill your needs.
    "notation_levels": {
        # Typically, some words are treated differently in titles, e.g. determining
        # words like "the", "any", etc. You may define them here for convenient use.
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
    # Define the correct notation for specific words. The first element in the
    # tuple denotes the correct version, the second lists various "evil twins".
    "notation_twins": [
        ("public key", ["public-key", "publickey", "pubkey"]),
        ("elliptic curve", ["elliptic-curve"])
    ],
    # Some words pass a spell-check, but may carry very different meaning. If you spot
    # some of them during writing, put them here to be prepared in the future. The first
    # part of the tuple is the "probably right" word.
    "confusing_words": [
        ("threat", ["thread"]),
        ("proposed", ["purposed"])
    ],
    # Define which checks to use. These checks are defined in `main.py? and can be
    # extended. Pull-requests to `https://github.com/duesee/pedanticpaper` are welcome.
    "checks": [
        "check_allowed_chars",
        "check_notation_levels",
        "check_twins",
        "check_confusing",
        "check_doubled_words",
    ]
}
