#!/bin/sh
./makeentries.py "../Sejong_1.txt" 
xelatex -pdf vocab-list.tex
mv vocab-list.pdf ..
xelatex flashcard.tex
mv flashcard.pdf ..
