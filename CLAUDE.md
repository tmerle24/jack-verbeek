# Jack Verbeek — Romanreihe

## Was das hier ist

Krimi-Action-Thriller-Reihe, open end. Deutsch.
Zielgruppe: breites Publikum, schnell lesbar, hoher Sog.

## Kontext zu Beginn jeder Session lesen

Vor der ersten Aufgabe einer Session immer lesen, in dieser Reihenfolge:

1. bible/bible.md            — Figuren, Orte, Reihenplanung
2. stil/stimme.md            — Ton, Regeln, Referenztext
3. band-01/plot.md           — Handlungsverlauf
4. band-01/arbeitsstand.md   — wo wir gerade stehen

Bei Widerspruch gilt: arbeitsstand.md schlägt plot.md,
stimme.md schlägt alles Übrige.

## Harte Regeln

- Kapitel: 3–6 Seiten, ohne Ausnahme. Jedes Kapitel endet auf einer Kante.
- Jack: Ich-Erzähler, Präteritum. Alle anderen: 3. Person personal.
  Niemals mischen.
- Technik nie erklären, immer zeigen. Wenn erklärt werden muss,
  erklärt Jack es Yuna.
- Gewalt: kalt, nie blutig. Der Schock kommt aus der Logik, nicht
  aus der Beschreibung.
- Am Ende bleibt ein positives Gefühl. Immer.

## Technik in Angriffs- und Zugriffsszenen

- Technik wird über Wirkung, Risiko und Körper erzählt, nie über das
  Verfahren. Was es mit Jack macht, nicht wie es geht.
- Kein Code im Fließtext. Keine realen Werkzeugnamen, keine
  Schwachstellenbezeichnungen, keine Befehlsfolgen.
- Keine nachvollziehbaren Schrittfolgen. Der Leser soll glauben, dass
  es funktioniert, nicht wissen, wie.
- Konkret sein bei: Zeit, Geräusch, Temperatur, Licht, Müdigkeit,
  Fehlschlägen. Vage bleiben bei: Verfahren.

## Arbeitsrhythmus

Gearbeitet wird in Blöcken, nicht in Tagen.

Ein Block =
  1. Blockplanung vorlegen und bestätigen lassen
  2. Kapitel schreiben, einzeln
  3. Review über den ganzen Block
  4. Korrekturen einarbeiten
  5. arbeitsstand.md aktualisieren
  6. Committen

Nach jedem Block endet die Session. Nicht mehrere Blöcke in einer
Session bearbeiten — der Kontext füllt sich, und frühe Anweisungen
werden von Zwischenergebnissen überlagert.

Nie mehr als ein Kapitel pro Antwort schreiben.
Vor einem neuen Block immer erst die Planung vorlegen, nie direkt
mit dem Schreiben beginnen.

## Kontinuität

Vor jedem Kapitel prüfen: Wochentag, Uhrzeit, Ort, wer wo ist,
welche Geräte Jack gerade hat, Alter der Kinder.

Widersprüche zur Bible nicht selbst auflösen, sondern melden.

Neue Namen, Orte und Firmen werden sofort in die Bible eingetragen,
nicht erst am Blockende.

## Arbeitsstand

`band-01/arbeitsstand.md` ist das Sessiongedächtnis. Sie enthält:

- Zuletzt geschriebene Kapitel und deren Reviewergebnis
- Offene Korrekturen mit Kapitelnummer
- Den nächsten geplanten Block mit Kapitelzweck
- Laufende Listen (Verpuffungen, offene Fäden, Namen)
- Entscheidungen, die vom Plot abweichen, mit Begründung

Wird am Ende jedes Blocks aktualisiert, vor dem Commit.
Kurz halten: Was erledigt ist, fliegt raus.
Ersetzt keine Planung, überbrückt Sessionwechsel.

## Dateikonvention

- Ein Kapitel pro Datei: band-01/kapitel/NNN.md
- Frontmatter je Kapitel: pov, ort, zeit, plot-funktion, schlusssatz

## Committen

- Keine Co-Authored-By-Zeile, keine Attribution, kein Tool-Hinweis.
- Format: kap(001): kurzbeschreibung
- Ein Commit pro Kapitel, ein zusätzlicher für den Arbeitsstand.
