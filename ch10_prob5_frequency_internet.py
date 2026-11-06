# Chapter 10, Problem 5 — Letter Frequency Analysis of a Book Downloaded From the Internet


import urllib.request
from graphics import *

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def downloadText(url):
    response = urllib.request.urlopen(url)
    rawBytes = response.read()
    response.close()
    text = rawBytes.decode("utf-8", errors="ignore")
    return text

def countLetters(text):
    counts = [0] * 26
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

def writeCounts(fileName, counts):
    outFile = open(fileName, "w")
    i = 0
    while i < 26:
        outFile.write(ALPHABET[i] + "," + str(counts[i]) + "\n")
        i = i + 1
    outFile.close()

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
        bar.setFill("tomato")
        bar.draw(win)

        label = Text(Point(i + 1, -0.015), ALPHABET[i])
        label.draw(win)

        i = i + 1

    win.getMouse()
    win.close()

def main():
    url = input("Enter the URL of a text file to download and analyze: ")
    outFileName = input("Enter an output file name to save the letter counts (e.g. counts.txt): ")

    text = downloadText(url)
    counts = countLetters(text)
    ratios = countsToRatios(counts)

    writeCounts(outFileName, counts)

    print()
    print("Letter", "\tCount", "\tRatio")
    i = 0
    while i < 26:
        print(ALPHABET[i], "\t", counts[i], "\t", round(ratios[i], 4))
        i = i + 1

    print()
    print("Letter counts written to", outFileName)

    drawGraph(ratios, "Letter Frequency: " + url)

main()
