#!/bin/sh
./makeentries.py "../Sejong1.txt" 
latexmk -pdf vocab-list.tex
mv vocab-list.pdf ..
latexmk -pdf flashcard.tex
mv flashcard.pdf ..
