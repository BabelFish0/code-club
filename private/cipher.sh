#!/bin/bash

MESSAGE="null"
SHIFT=1
SEED=0

while [ $SEED -le 10 ]; do
    python3 caesar.py "$MESSAGE" $SHIFT $SEED
    pdflatex encoded_message.tex
    mv encoded_message.pdf encoded_message"$SEED".pdf
    ((SEED++))
done