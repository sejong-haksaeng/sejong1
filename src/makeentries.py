#!/usr/bin/env python2
import fileinput

#template = """
#\\newglossaryentry{%s}
#{
#    name={%s},
#    description={%s}
#}
#"""
template = """
\\textbf{%s} : %s
"""

with open('glossaryentries.tex', 'wb') as f:
    for line in fileinput.input():
        q, a = line.rstrip('\n').split('\t', 1)
        f.write(template % (q, a))

template = """
\\begin{flashcard}{%s}
\\vspace*{\stretch{1}}
%s
\\vspace*{\stretch{1}}
\end{flashcard}
"""

with open('flashcards.tex', 'wb') as f:
    for id, line in enumerate(fileinput.input()):
        q, a = line.rstrip('\n').split('\t', 1)
        f.write(template % (q, a))
