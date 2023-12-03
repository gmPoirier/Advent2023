# Advent of Code 2023: Star 02
#=============================
# Takes a document with lines of text and outputs a single integer
# Each line containes a number that sums to the output integer
# The number from each line is found by using the first digit in the line 
# as the tens place and the last digit in the line as the ones place

# Currently bugged so that a digit number immediately preceding a text number 
# caused the program to not see the text number
# ex: 5fivezgfgcxbf3five    [(1, '5'), (1, '5')] 	 53

def find_text_digits(line):
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    lowest_index = len(line)
    digit_at_lowest = ""

    highest_index = -1
    digit_at_highest = ""

    for i in range(len(digits)):
        index_low = line.find(digits[i])
        if index_low > -1:
            if index_low < lowest_index:
                lowest_index = index_low
                digit_at_lowest = i

        index_high = line.rfind(digits[i])
        if index_high > -1:
            if index_high > highest_index:
                highest_index = index_high
                digit_at_highest = i

    return [(lowest_index, str(digit_at_lowest)),(highest_index, str(digit_at_highest))]

def main():
    file = open("input/day_01.txt", "r", encoding="utf-8")
    output = 0

    for line in file:
        digits = find_text_digits(line)

        tens = -1
        ones = -1
        # loop forwards thru the line to find the first digit
        for i in range(digits[0][0]):
            if line[i].isdigit():
                tens = line[i]
                break
        if tens == -1:
            tens = digits[0][1]
        # loop backwards thru the line to find the last digit
        for i in reversed(range(len(line))):
            if i > digits[1][0]:
                if line[i].isdigit():
                    ones = line[i]
                    break
        if ones == -1:
            ones = digits[1][1]

        line_digit = int(tens + ones)
        print(line, find_text_digits(line), "\t", line_digit)
        output += line_digit

    print(output)

if __name__ == "__main__":
    main()
