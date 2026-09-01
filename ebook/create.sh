#!/bin/bash

# 1. Kapitel bereinigen (löscht Frontmatter pro Datei, ignoriert --- im Text)
awk 'FNR==1{in_front=0} FNR==1 && /^---$/{in_front=1; next} in_front && /^---$/{in_front=0; next} !in_front' \
    ../band-01/kapitel/*.md > temp_kapitel.md

# 2. Die beiden reinen Markdown-Dateien zusammenfügen
pandoc titel.md temp_kapitel.md -o jack-verbeek-01.pdf --pdf-engine=weasyprint --css=style.css

# 3. Aufräumen
rm temp_kapitel.md
