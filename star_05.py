# Advent of Code 2023: Star 05
#=============================
# Given an file with lines of text, ouput a single integer
import re

def main():
    file = open("input/day_03.txt", "r", encoding="utf-8")
    num = re.compile('[0-9]+')
    sym = re.compile('[^a-zA-Z0-9\.]+')
    prev = ""

    # I have realized I can just keep track of the current and previous
    # line and use a regex to find any all digit substrings and then get
    # the indices and check the corresponding substring of the previous 
    # line for symbols. Similarly, I can search a string for symbols and
    # Then check the previous string for any digits an the proper indices
    for line in file:
        if prev == "":
            prev = line

        numbers = num.finditer(line)
        for match in numbers:
            loc = match.span()
            if sym.search(prev, loc[0], loc[1]):
                print(match)

        prev = line

    file.close
    return 0

if __name__ == "__main__":
    main()
