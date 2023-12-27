
def main():

    inputFile = open('input.txt', 'r').readlines()
    lineNumbers = []
    numberText = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                  'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    for line in inputFile:
        firstNumber = None
        lastNumber = None
        for char1 in range(0, len(line)):
            if 48 <= ord(line[char1]) <= 57:
                firstNumber = line[char1]
                break
            elif (num := line[char1:char1 + 3]) in numberText:
                firstNumber = numberText[num]
                break
            elif (num := line[char1:char1 + 4]) in numberText:
                firstNumber = numberText[num]
                break
            elif (num := line[char1:char1 + 5]) in numberText:
                firstNumber = numberText[num]
                break

        for char2 in range(len(line) - 1, -1, -1):
            if 48 <= ord(line[char2]) <= 57:
                lastNumber = line[char2]
                break
            elif (num := line[char2 - 2:char2 + 1]) in numberText:
                lastNumber = numberText[num]
                break
            elif (num := line[char2 - 3:char2 + 1]) in numberText:
                lastNumber = numberText[num]
                break
            elif (num := line[char2 - 4:char2 + 1]) in numberText:
                lastNumber = numberText[num]
                break
            
        lineNumbers.append(int(firstNumber + lastNumber))

    print(sum(lineNumbers))

main()