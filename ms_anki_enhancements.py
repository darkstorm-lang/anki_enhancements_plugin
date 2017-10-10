"""
Simple anki plugin to allow case insensitive spelling comparisions and to
optionally ignore sections in the answer that are surrounded by user defined
symbols ('[' and ']') by default. This means that 'Hello' will correctly match
'heLLo[bob]'.

Author: Martin Slater
Email: mslater@hellinc.net

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""
from aqt.reviewer import Reviewer
import re

# If this is true then any elements in the correct text surrounded by the strings
# in the Marks array below will be ignored for comparison purposes.
IgnoreMarkedSections = True
Marks = [ '[', ']' ]

def patched_correct(self, given, correct, showBad):
    if IgnoreMarkedSections:
        # remove any sections in the correct answer that are surrounded by the user marks
        correct = re.sub(re.escape(Marks[0]) + '.*' + re.escape(Marks[1]), '', correct, 0, re.MULTILINE)

    return original_correct(self, given.lower(), correct.lower(), showBad)

original_correct = Reviewer.correct
Reviewer.correct = patched_correct

