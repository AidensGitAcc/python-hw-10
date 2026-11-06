# Chapter 10, Problem 3 — Letter Frequency Analysis With a Graph


from graphics import *

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def countLetters(fileName):
    counts = [0] * 26
    inFile = open(fileName, "r")
    text = inFile.read()
    inFile.close()

    text = text.lower()
    i = 0
    while i < len(text):
        ch = text[i]
        if ch.isalpha() and ch in ALPHABET:
            index = ALPHABET.index(ch)
            counts[index] = counts[index] + 1
        i = i + 1
    return counts

def countsToRatios(counts):
    total = 0
    i = 0
    while i < len(counts):
        total = total + counts[i]
        i = i + 1

    ratios = []
    i = 0
    while i < len(counts):
        if total > 0:
            ratios.append(counts[i] / total)
        else:
            ratios.append(0)
        i = i + 1
    return ratios

def drawGraph(ratios, title):
    maxRatio = 0
    i = 0
    while i < len(ratios):
        if ratios[i] > maxRatio:
            maxRatio = ratios[i]
        i = i + 1

    if maxRatio == 0:
        maxRatio = 0.01

    win = GraphWin(title, 900, 500)
    win.setBackground("white")
    win.setCoords(0, -0.03, 27, maxRatio * 1.15)

    heading = Text(Point(13.5, maxRatio * 1.08), title)
    heading.setSize(14)
    heading.draw(win)

    i = 0
    while i < 26:
        left = i + 0.6
        right = i + 1.4
        bar = Rectangle(Point(left, 0), Point(right, ratios[i]))
        bar.setFill("cornflowerblue")
        bar.draw(win)

        label = Text(Point(i + 1, -0.015), ALPHABET[i])
        label.draw(win)

        i = i + 1

    win.getMouse()
    win.close()

def main():
    fileName = input("Enter the name of a text file to analyze: ")
    counts = countLetters(fileName)
    ratios = countsToRatios(counts)

    print()
    print("Letter", "\tCount", "\tRatio")
    i = 0
    while i < 26:
        print(ALPHABET[i], "\t", counts[i], "\t", round(ratios[i], 4))
        i = i + 1

    drawGraph(ratios, "Letter Frequency: " + fileName)

main()
