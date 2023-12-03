# Advent of Code 2023: Star 04
#=============================
# Takes a document with lines of text and outputs an single integer
# Each line represents a number of games where cubes are pulled from a bag
# Given a bag with a certain number of each color of cube, what is the fewest
# number of each colored cube to make the game possible?
# Multiply the minimum number of each color cube together to get a game's power
# Sum the powers of every game to get the output integer

def get_minimum_cubes(game):
    min_reds = 0
    min_greens = 0
    min_blues = 0

    draws = str(game).split(";")

    for draw in draws:
        cubes = draw.split(",")
        
        for cube in cubes:
            cube = cube.strip()
            num_cubes = int(cube.split(" ")[0])
            if "red" in cube:
                if num_cubes > min_reds:
                    min_reds = num_cubes
            elif "green" in cube:
                if num_cubes > min_greens:
                    min_greens = num_cubes
            elif "blue" in cube:
                if num_cubes > min_blues:
                    min_blues = num_cubes

    return (min_reds, min_greens, min_blues)

def get_game_data(game):
    raw_id_draws_list = game.split(":")

    raw_game_id = raw_id_draws_list[0]
    raw_draws = raw_id_draws_list[1]

    game_id = raw_game_id.removeprefix("Game ")
    game_id = int(game_id)

    draws = raw_draws.strip()

    return (game_id, draws)

def main():
    file = open("input/day_02.txt", "r", encoding="utf-8")
    sum_power = 0

    for game in file:
        power = 1
        game_data = get_game_data(game)
        
        for cubes in get_minimum_cubes(game_data[1]):
            power = power * cubes

        sum_power += power

    file.close()
    print(sum_power)

if __name__ == "__main__":
    main()
