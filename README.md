# Tetris in Pygame

Dies ist eine einfache Implementierung des klassischen Spiels **Tetris** in Python mit der **Pygame**-Bibliothek. Das Spiel ermöglicht es, Tetrominos zu bewegen, zu rotieren und Linien zu löschen, wenn sie vollständig gefüllt sind.

## Inhaltsverzeichnis

1. [Spielprinzip](#spielprinzip)
2. [Hauptfunktionen](#hauptfunktionen)
3. [Code-Erklärung](#code-erklärung)
4. [Anleitung zum Ausführen des Programms](#anleitung-zum-ausführen-des-programms)

---

## Spielprinzip

Das Spiel besteht aus einem Spielfeld, auf dem **Tetrominos** (Tetris-Steine) von oben nach unten fallen. Diese Tetrominos haben verschiedene Formen und müssen in das Spielfeld eingefügt werden, um vollständige Reihen zu bilden. Wenn eine vollständige Reihe entsteht, wird sie entfernt, und die darüber liegenden Blöcke fallen nach unten. Das Ziel ist es, so viele Reihen wie möglich zu löschen, bevor der Bildschirm voll wird.

Das Spiel endet, wenn ein Tetromino den oberen Rand des Spielfelds erreicht.

---

## Hauptfunktionen

### Tetrominos

Tetrominos sind die Bausteine des Spiels. Es gibt 7 verschiedene Formen, die jeweils aus 4 kleinen Blöcken bestehen. Diese können sich nach links, rechts und nach unten bewegen und um 90° rotiert werden.

### Spielfeld

Das Spielfeld besteht aus einem Gitter, das in Zellen unterteilt ist. Jede Zelle kann entweder aktiv (mit einem Tetromino besetzt) oder leer sein. Wenn eine vollständige Zeile von Zellen besetzt ist, wird diese gelöscht und die darüber liegenden Zellen rutschen nach unten.

### Reihen löschen

Wenn eine Reihe vollständig ausgefüllt ist, wird sie gelöscht und alle darüber liegenden Zellen werden nach unten verschoben, um Platz für neue Tetrominos zu schaffen.

---

## Code-Erklärung

### TetrisBoard

Die Klasse `TetrisBoard` repräsentiert das Spielfeld. Sie verwaltet die Gitterstruktur und stellt Methoden zum Zeichnen und Verwalten von Zellen zur Verfügung. Es enthält auch die Logik zum Zeichnen des Spielfelds und der Zellen.

### Tetromino

Die Klasse `Tetromino` repräsentiert die Tetris-Steine. Jeder Stein hat eine Form (Matrix) und eine Farbe. Es enthält Methoden zur Bewegung, Rotation und Kollisionsprüfung der Tetrominos innerhalb des Spielfelds.

### Reihen löschen und verschieben

Wenn eine Reihe vollständig ist, wird sie gelöscht und die darüber liegenden Blöcke werden nach unten verschoben. Dies geschieht durch die Funktionen `clear_lines` und `drop_rows`, die alle vollständigen Reihen erkennen und die darüber liegenden Zellen entsprechend verschieben.

---

## Anleitung zum Ausführen des Programms

### Voraussetzungen

Um das Spiel auszuführen, müssen Sie Python und die Pygame-Bibliothek installiert haben. Falls Pygame noch nicht installiert ist, können Sie es mit dem folgenden Befehl installieren:

```bash
pip install pygame
```

### Ausführen des Programms
1. Klonen oder laden Sie das Repository herunter.
2. Navigieren Sie zum Verzeichnis des Projekts.
3. Starten Sie das Spiel mit dem folgenden Befehl:
```bash
python tetris_main.py
```
---

## Steuerung
- Pfeil links: Bewegt das Tetromino nach links.
- Pfeil rechts: Bewegt das Tetromino nach rechts.
- Pfeil runter: Bewegt das Tetromino schneller nach unten.
- Pfeil hoch: Rotiert das Tetromino um 90 Grad.

---

ReadMe.md wurde mit AI unterstützung geschrieben.
