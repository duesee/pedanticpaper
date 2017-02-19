import string
import json


def load_json(path):
    return json.load(open(path, "rt"))


config = {
    "regex_doublettes": r"\b(\w+)\b\s+\b(\1)\b",
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
