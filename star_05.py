# Advent of Code 2023: Star 05
#=============================
# Given an file with lines of text, ouput a single integer
import re

def main():
    file = open("input/day_03.txt", "r", encoding="utf-8")
    num = re.compile('[0-9]+')
    sym = re.compile('[^a-zA-Z0-9\.\n]+')
    prev = ""
    out = 0

    # I have realized I can just keep track of the current and previous
    # line and use a regex to find any all digit substrings and then get
    # the indices and check the corresponding substring of the previous 
    # line for symbols. Similarly, I can search a string for symbols and
    # Then check the previous string for any digits an the proper indices
    for line in file:
        line_out = ""
        numbers = num.finditer(line)
        for match in numbers:

            loc = match.span()
            start = loc[0]
            end = loc[1]

            if loc[0] > 0:
                start = loc[0] - 1
            if loc[1] < len(line) - 1:
                end = loc[1] + 1

            if prev != "":
                if sym.search(prev, start, end):
                    line_out += match.group(0) + " "
                    out += int(match.group(0))
            if sym.search(line, start, end):
                line_out += match.group(0) + " "
                out += int(match.group(0))

        symbols = sym.finditer(line)
        for match in symbols:

            loc = match.span()
            start = loc[0]
            end = loc[1]

            if loc[0] > 0:
                start = loc[0] - 1
            if loc[1] < len(line) - 1:
                end = loc[1] + 1

            if prev != "":
                if num.search(prev, start, end):
                    prev_nums = num.finditer(prev)
                    for number in prev_nums:
                        loc = number.span()
                        if start < loc[1] and end > loc[0]:
                            line_out += number.group(0) + " "
                            out += int(number.group(0))

        prev = line
        print(line_out)

    print(out)

    file.close
    return 0

if __name__ == "__main__":
    main()
