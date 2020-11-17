# Author: Govind Gnanakumar

import re

# needs optimizations for larger lists, like:
# asynchronously filtering suggestions so not all of them are pupulated at once
# or just showing some x top results rather than all of them at once
# add smartcase stuff
# populate with possible words

collection = []


def fuzzyfinder(user_input, collection):
    suggestions = []
    pattern = ".*?".join(user_input)
    regex = re.compile(pattern)
    for item in collection:
        match = regex.search(item)
        if match:
            suggestions.append((len(match.group()), match.start(), item))
    return [x for _, _, x in sorted(suggestions)]
