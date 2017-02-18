# Pedanticpaper

This script should spot several mistakes in TeX files, a spell-checker won't. For it to work, a configuration file must be defined.

Currently, the tool does the following:

* Find "evil twins", e.g. to evaluate that the word "side-channel" was always used instead of "side channel" or "sidechannel".
* Check for consistency in the title of section-, subsection-, etc., e.g. "How to write Research Papers" (upper-case style) vs. "How to write research papers" (lower-case style).
* Warn on potentially confusing words like "proposed" vs "purposed".
* Find doublettes, i.e. "We showed that that..."
* Find characters not on a whitelist, i.e. difficult to spot unicode characters, which may introduce parsing errors.

The script does not change any files. In fact, only `open(file, "rt")` is used. Each modification must be manually applied.
