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
    # in TeX files. We find the given definition suitable for german texts.
    "allowed_chars": string.printable + "ÄÖÜäöüß",
    # Define the notation for section, subsection, etc., e.g.
    # upper- "My Research Paper" vs lower-case "My research paper".
    # The function bodies at the top can be defined to fulfill your needs.
    "notation_levels": {
        # Typically, some words are treated differently in titles, e.g.
        # determiner like "the", "any", etc. Define them here for convenient use.
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
    # Define the notation to be used for specific words. The first element in
    # the tuple denotes the correct version, the second is a list of "evil twins".
    "notation_twins": [
        ("public key", ["public-key", "publickey", "pubkey"]),
        ("elliptic curve", ["elliptic-curve"])
    ],
    # Some words will pass a spell-checking, but may carry very different meaning.
    # If you spot some of them during your work on a document, put them here to be
    # prepared in the future.
    "confusing_words": [
        ("threat", ["thread"]),
        ("proposed", ["purposed"])
    ],
    # Define which checks to use? These checks are defined in main and can be extended.
    "checks": [
        "check_allowed_chars",
        "check_notation_levels",
        "check_twins",
        "check_confusing",
        "check_doubled_words",
    ]
}
