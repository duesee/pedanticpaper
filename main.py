#!/usr/bin/env python3
#

from config import *

import re
import os
import sys


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
            print('[S] found potentially inconsistent {:<13} {:<60}'.format(level, '"{}"'.format(title)))


def check_allowed_chars(text):
    for lineno, line in enumerate(text.splitlines()):
        for char in line:
            if char not in config["allowed_chars"]:
                print("[!] found non-allowed char '{}' in line {}".format(char, lineno + 1))


def check_doubled_words(text):
    doublettes = re.compile(r"\s+(\w+)\s+(\1)\s+")
    for lineno, line in enumerate(text.splitlines()):
        for doublette in doublettes.findall(line):
            (g1, g2) = doublette
            print('[D] found doublette "{} {}" in line {}'.format(g1, g2, lineno + 1))


def check_twins(text):
    for lineno, line in enumerate(text.splitlines()):
        for (good, bad) in config["notation_twins"]:
            for twin in bad:
                if twin in line.lower():
                    print('[T] found evil twin "{}" in line {}. Did you mean "{}"?'.format(twin, lineno + 1, good))


def check_confusing(text):
    for lineno, line in enumerate(text.splitlines()):
        for (expected, confusing) in config["confusing_words"]:
            for word in confusing:
                if word in line:
                    print('[?] found potentially confusing word "{}" in line {}. Did you mean "{}"?'.format(word, lineno + 1, expected))


def check_weasel_words(text):
    for lineno, line in enumerate(text.splitlines()):
        for word in config["weasel_words"]:
            if word in line:
                print('[W] found weasle word "{}" in line {}. Can it be clarified?'.format(word, lineno + 1))


def check_abbrev(text):
    for lineno, line in enumerate(text.splitlines()):
        for (correct, erroneous) in config["wrong_abbrev"]:
            for word in erroneous:
                if word in line:
                    print('[A] found erroneous abbreviation "{}" in line {}. Did you mean "{}"?'.format(word, lineno + 1, correct))


if __name__ == "__main__":
    path = "./" if len(sys.argv) < 2 else sys.argv[1]
    print('### Starting recursive search from "{}"'.format(path))

    for file in walk_tex(path):
        print('### Testing file "{}"'.format(file))
        with open(file, "r") as file:
            file = file.read()
            for check in config["checks"]:
                 locals()[check](file)
        print()