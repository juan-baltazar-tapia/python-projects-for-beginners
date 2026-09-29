import random

WINNING_SCORE = 20
def display_totals(total, player_one_score, player_two_score):
    print(" ")
    print(f"You scored {total} points this turn.")
    print(
        f"Current scores: Player 1: {player_one_score} Player 2: {player_two_score} \n"
    )


def display_winner(player_turn, player_one_score, player_two_score):
    points = player_one_score if player_turn == 0 else player_two_score
    print(f"Player {player_turn + 1} won! with {points} points")


def take_turn(player_turn, player_one_score, player_two_score):
    curr_total = 0
    current_player_score = player_one_score if player_turn == 0 else player_two_score

    while True:
        dice_roll = random.randint(1, 6)
        if dice_roll == 1:
            print("You rolled a 1, 0 points.")
            # display_totals(0, PLAYER_ONE_SCORE, PLAYER_TWO_SCORE)
            curr_total = 0
            break
        curr_total += dice_roll
        print(f"You rolled a {dice_roll}")
        if curr_total + current_player_score >= WINNING_SCORE:
            break
        user_input = input("Roll again? (y/n): ")
        if user_input == "n":
            break
    if player_turn == 0:
        player_one_score += curr_total
    else:
        player_two_score += curr_total
    display_totals(curr_total, player_one_score, player_two_score)

    return player_one_score, player_two_score


def main():
    current_player = 0
    player_one_score = 0
    player_two_score = 0
    while True:
        print(f"Player {current_player % 2 + 1}'s turn")
        player_one_score, player_two_score = take_turn(
            current_player % 2, player_one_score, player_two_score
        )
        if player_one_score >= WINNING_SCORE or player_two_score >= WINNING_SCORE:
            break
        
        current_player += 1
    display_winner(current_player % 2, player_one_score, player_two_score)


if __name__ == "__main__":
    main()
