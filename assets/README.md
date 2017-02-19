### Define allowed characters.

Detect characters, e.g. unicode chars, which may introduce subtle errors in TeX files.

### Detect evil twins.

Define the correct notation for specific words. The first element in the tuple denotes the correct version,
the second is a lists of various "evil twins".

### Find wrong abbreviations.

The same `[good, [bad1, bad2, ...]]` pattern applies as in evil twins.

### Find potentially confusing words.

Some words pass a spell-check, but may carry very different meaning. If you spot some of them
during writing, put them here to be prepared in the future. The first part of the tuple is the
"probably right" word -- use `""` if there is none.

### Find leftovers in text.

Make sure there are no leftovers, e.g. "todo", "tbd", etc. Matching is case-insensitive.

### Find weasel words.

"A weasel word (...) is an informal term for words and phrases aimed at creating an
impression that a specific or meaningful statement has been made, when instead only
a vague or ambiguous claim has actually been communicated." (https://en.wikipedia.org/wiki/Weasel_word)

### Find the use of passive voice.

"The passive voice is a grammatical construction (specifically, a "voice"). The noun or noun phrase that
would be the object of an active sentence (such as Our troops defeated the enemy) appears as the subject
of a sentence or clause in the passive voice (e.g. The enemy was defeated by our troops)." (https://en.wikipedia.org/wiki/English_passive_voice)

### Thanks

Some of the list were taken from http://matt.might.net/articles/shell-scripts-for-passive-voice-weasel-words-duplicates/.
