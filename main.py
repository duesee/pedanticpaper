#!/usr/bin/env python3
#

from config import *

import re
import os


def find_match(data, regex):
    expr = re.compile(regex)
    for match in re.findall(expr, data):
        yield match


def walk_tex(path):
    def is_tex(path):
        if not os.path.isfile(path):
            return False
        extension = os.path.basename(path).split(".")[-1]
        return extension.lower() == "tex"

    for root, dirs, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)
            if is_tex(path):
                yield os.path.abspath(path)


def check_notation_levels(text):
    for match in find_match(file, r"\\(section|subsection|subsubsection|paragraph|subparagraph){(.*?)}"):
        (level, title) = match
        if not config["notation_levels"][level](title):
            print('[?] found potentially inconsistent {:<13} "{:<60}"'.format(level, title))


def check_allowed_chars(text):
    for lineno, line in enumerate(text.splitlines()):
        for char in line:
            if char not in config["allowed_chars"]:
                print("[!] found non-allowed char '{}' in line {}".format(char, lineno + 1))


def check_doubled_words(text):
    doublettes = re.compile(r"\s+(\w+)\s+(\1)\s+")
    for lineno, line in enumerate(text.splitlines()):
        for doublette in doublettes.findall(line):
            print("[!] found doublette {} in line {}".format(doublette, lineno + 1))


def check_twins(text):
    for lineno, line in enumerate(text.splitlines()):
        for (good, bad) in config["notation_twins"]:
            for twin in bad:
                if twin in line.lower():
                    print('[!] found evil twin "{}" in line {}. Did you mean "{}"?'.format(twin, lineno + 1, good))


def check_confusing(text):
    for lineno, line in enumerate(text.splitlines()):
        for (expected, confusing) in config["confusing_words"]:
            for word in confusing:
                if word in line:
                    print('[?] found potentially confusing word "{}" in line {}. Did you mean "{}"?'.format(word, lineno + 1, expected))


if __name__ == "__main__":
    for file in walk_tex("test"):
        print("### Testing file {}".format(file))
        with open(file, "r") as file:
            file = file.read()
            for check in config["checks"]:
                 locals()[check](file)
        print()