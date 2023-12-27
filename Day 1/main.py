
def main():

    inputFile = open('input.txt', 'r').readlines()
    lineNumbers = []

    for line in inputFile:
        firstNumber = None
        lastNumber = None
        for char1 in line:
            if 48 <= ord(char1) <= 57:
                firstNumber = char1
                break
        for char2 in range(len(line) - 1, -1, -1):
            if 48 <= ord(line[char2]) <= 57:
                lastNumber = line[char2]
                break

        lineNumbers.append(int(firstNumber + lastNumber))

    print(sum(lineNumbers))

main()