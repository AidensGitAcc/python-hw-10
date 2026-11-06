# Chapter 10, Problem 1 — Amortization Report to a File

def calcPmt(P0, r, k, N):
    d = P0 / ((1 - (1 + r / k) ** (-N * k)) / (r / k))
    return d

def writeReport(fileName, p0, r, k, n):
    payment = calcPmt(p0, r, k, n)
    totalPayments = n * k
    balance = p0

    outFile = open(fileName, "w")

    outFile.write("Payment #" + "\tPayment" + "\tInterest" + "\tPrincipal" + "\tBalance Remaining" + "\n")

    paymentNum = 1
    while paymentNum <= totalPayments:
        interest = balance * (r / k)
        principal = payment - interest
        balance = balance - principal

        line = str(paymentNum) + "\t" + str(round(payment, 2)) + "\t" + str(round(interest, 2)) + "\t" + str(round(principal, 2)) + "\t" + str(round(balance, 2)) + "\n"
        outFile.write(line)

        paymentNum = paymentNum + 1

    outFile.close()

def main():
    p0 = float(input("Enter the amount to finance: "))
    r = float(input("Enter the annual interest rate (as a decimal): "))
    k = int(input("Enter the number of compounding periods per year: "))
    n = int(input("Enter the number of years: "))
    fileName = input("Enter the output file name (e.g. report.txt): ")

    writeReport(fileName, p0, r, k, n)

    print()
    print("Amortization report written to", fileName)

main()
