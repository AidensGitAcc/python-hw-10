# Chapter 10, Problem 2 — Path-From-File Cipher

import random

def readPathFile(fileName):
    inFile = open(fileName, "r")
    firstLine = inFile.readline()
    parts = firstLine.split(",")
    numRows = int(parts[0])
    numCols = int(parts[1])

    path = []
    line = inFile.readline()
    while line != "":
        line = line.strip()
        if line != "":
            coords = line.split(",")
            row = int(coords[0])
            col = int(coords[1])
            path.append((row, col))
        line = inFile.readline()

    inFile.close()
    return numRows, numCols, path

def padMessage(message, totalLength):
    while len(message) < totalLength:
        message = message + chr(random.randint(65, 90))
    return message

def buildGrid(message, numRows, numCols):
    grid = []
    index = 0
    row = 0
    while row < numRows:
        newRow = []
        col = 0
        while col < numCols:
            newRow.append(message[index])
            index = index + 1
            col = col + 1
        grid.append(newRow)
        row = row + 1
    return grid

def encipher(message, numRows, numCols, path):
    message = message.upper()
    totalLength = numRows * numCols
    message = padMessage(message, totalLength)
    grid = buildGrid(message, numRows, numCols)

    ciphertext = ""
    i = 0
    while i < len(path):
        row, col = path[i]
        ciphertext = ciphertext + grid[row][col]
        i = i + 1
    return ciphertext

def decipher(ciphertext, numRows, numCols, path):
    grid = []
    row = 0
    while row < numRows:
        newRow = []
        col = 0
        while col < numCols:
            newRow.append("")
            col = col + 1
        grid.append(newRow)
        row = row + 1

    i = 0
    while i < len(path):
        row, col = path[i]
        grid[row][col] = ciphertext[i]
        i = i + 1

    plaintext = ""
    row = 0
    while row < numRows:
        col = 0
        while col < numCols:
            plaintext = plaintext + grid[row][col]
            col = col + 1
        row = row + 1
    return plaintext

def main():
    pathFileName = input("Enter the name of the file containing the grid size and path: ")
    numRows, numCols, path = readPathFile(pathFileName)

    message = input("Enter a message to encipher (no spaces): ")

    cipher = encipher(message, numRows, numCols, path)
    print()
    print("Enciphered message:", cipher)

    plain = decipher(cipher, numRows, numCols, path)
    print("Deciphered message (includes random padding):", plain)

main()
