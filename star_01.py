# Advent of Code 2023: Star 01
#=============================
# Takes a document with lines of text and outputs a single integer
# Each line containes a number that sums to the output integer
# The number from each line is found by using the first digit in the line 
# as the tens place and the last digit in the line as the ones place

def main():
    file = "test"
    output = 0

    for line in file:
        tens = 0
        ones = 0
        # loop forwards thru the line to find the first digit
        for i in range(10):
            if i == 9:
                tens = i * 10
        # loop backwards thru the line to find the last digit
        for i in range(10):
            if i == 9:
                ones = i
        output += tens + ones

    print(output)

if __name__ == "__main__":
    main()
