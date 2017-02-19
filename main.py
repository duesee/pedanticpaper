#!/usr/bin/env python3
#

from config import *

from collections import defaultdict
import re
import os
import sys


def find_match(data, regex):
    expr = re.compile(regex, flags=re.MULTILINE)
    for match in re.finditer(expr, data):
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


def lineno(match, text):
    return text.count(os.linesep, 0, match.start()) + 1


def check_allowed_chars(text, results):
    for lineno, line in enumerate(text.splitlines(), 1):
        for char in line:
            if char not in config["allowed_chars"]:
                results[lineno].append("found non-allowed char '{}'.".format(char))


def find_via_regex(text, results, wordlist, message, correct=None):
    for word in wordlist:
        for match in find_match(text, word):
            if correct:
                if match.group(0) != correct:
                    results[lineno(match, text)].append(message.format(match.group(0), correct))
            else:
                results[lineno(match, text)].append(message.format(match.group(0)))


def check_confusing(text, results):
    for (correct, erroneous) in config["confusing_words"]:
        for word in erroneous:
            for match in find_match(text, word):
                if correct and match.group(0) != correct:
                    results[lineno(match, text)].append('found potentially confusing word "{}". Did you mean "{}"?'.format(match.group(0), correct))
                else:
                    results[lineno(match, text)].append('found potentially confusing word "{}". Please be careful.'.format(match.group(0)))


def check_doubled_words(text, results):
    for match in find_match(text, config["regex_doublettes"]):
        results[lineno(match, text)].append('found doublette "{} {}".'.format(match.group(1), match.group(2)))


def check_evil_twins(text, results):
    for (correct, erroneous) in config["evil_twins"]:
        find_via_regex(text, results, erroneous, 'found evil twin "{}". Did you mean "{}"?', correct=correct)


def check_abbrev(text, results):
    for (correct, erroneous) in config["wrong_abbrev"]:
        find_via_regex(text, results, erroneous, 'found erroneous abbreviation "{}". Did you mean "{}"?', correct=correct)


def check_denied_words(text, results):
    find_via_regex(text, results, config["denied_words"], 'found denied word "{}". Please resolve it.')


def check_weasel_words(text, results):
    find_via_regex(text, results, config["weasel_words"], 'found weasel word "{}". Can it be clarified?')


def check_passive_voice(text, results):
    find_via_regex(text, results, config["passive_voice"], 'found passive voice "{}". Can it be clarified?')


def print_results(tests):
    for path, results in sorted(tests.items()):
        if len(results):
            print('File "{}:"'.format(path))
            for lineno, warnings in sorted(results.items()):
                for warning in sorted(warnings):
                    print("\tLine {}: {}".format(lineno, warning))
            print()


if __name__ == "__main__":
    path = "./" if len(sys.argv) < 2 else sys.argv[1]
    print('Starting recursive search from "{}"'.format(path))

    tests = {}

    for file in walk_tex(path):
        results = defaultdict(lambda: [])
        with open(file, "r") as data:
            data = data.read()
            for check in config["checks"]:
                 locals()[check](data, results)
        tests[file] = results

    print_results(tests)