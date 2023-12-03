# Advent of Code 2023: Star 02
#=============================
# Takes a document with lines of text and outputs an single integer
# Each line represents a number of games where cubes are pulled from a bag
# Given a bag with a certain number of each color of cube, which games listed
# are possible?
# Sum the IDs of possible games to get the output integer

# Given set of cubes
RED = 12
GREEN = 13
BLUE = 14

def is_possible(game):
    draws = game.split(";")

    for draw in draws:
        cubes = draw.split(",")
        
        for cube in cubes:
            num_cubes = int(cube.split(" ")[0])
            if "red" in cube:
                if num_cubes > RED:
                    return false
            elif "green" in cube:
                if num_cubes > GREEN:
                    return false
            elif "blue" in cube:
                if num_cubes > BLUE:
                    return false

    return true

def main():
    file = open("input/day_02.txt", "r", encoding="utf-8")
    sum_possible_ids = 0

    for game in file:
        game_id = 0
        if is_possible(game):
            sum_possible_ids += game_id

    file.close()
    print(sum_possible_ids)

if __name__ == "__main__":
    main()
