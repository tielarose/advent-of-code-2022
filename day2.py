# def decrypt_strategy(char):
#     """Interprets a coded move and returns the value of that move in English"""

#     code = {'A': 'rock',
#             'B': 'paper',
#             'C': 'scissors',
#             'X': 'rock',
#             'Y': 'paper',
#             'Z': 'scissors'}

#     return code[char]


# def determine_win_loss_draw(player1_move, player2_move):
#     "Takes in two strings: player1's move and player2's move; returns whether it was a draw, win or loss for player2"
#     if player1_move == player2_move:
#         return 'draw'
#     elif player1_move == 'rock' and player2_move == 'paper':
#         return 'win'
#     elif player1_move == 'paper' and player2_move == 'scissors':
#         return 'win'
#     elif player1_move == 'scissors' and player2_move == 'rock':
#         return 'win'
#     else:
#         return 'loss'


# def calculate_points(player1_move, player2_move):
#     """Calculates the points for player2 in a round of rock-paper-scissors, based on the following point values:

#         rock = 1 point
#         paper = 2 points
#         scissors = 3 points

#         loss = 0 points
#         draw = 3 points
#         win = 6 points
#     """

#     move_points = {
#         'rock': 1,
#         'paper': 2,
#         'scissors': 3
#     }

#     result_points = {
#         'loss': 0,
#         'draw': 3,
#         'win': 6
#     }

#     player2_points = 0

#     game_result = determine_win_loss_draw(player1_move, player2_move)
#     player2_points += result_points[game_result]

#     player2_points += move_points[player1_move]

#     return player2_points


# def total_points_from_strategy_file(filepath):
#     """processes a file of game strategy, returns a point total"""

#     file = open(filepath)

#     points_total = 0

#     for line in file:
#         line = line.rstrip().split()
#         print(f'Total was {points_total}')
#         player1_move = decrypt_strategy(line[0])
#         player2_move = decrypt_strategy(line[1])
#         points_total += calculate_points(player1_move, player2_move)
#         print(
#             f'total is now {points_total}. P1 played {player1_move}, P2 played {player2_move}')

#     return points_total


def total_points_from_strategy_file(filepath):
    """processes a file of game strategy, returns a point total"""

    file = open(filepath)

    points_total = 0

    round_value = {
        ('A', 'X'): 4,  # rock, rock -> (1 + 3 = 4)
        ('A', 'Y'): 8,  # rock, paper -> (2 + 6 = 8)
        ('A', 'Z'): 3,  # rock, scissors -> (3 + 0 = 3)
        ('B', 'X'): 1,  # paper, rock -> (1 + 0 = 1)
        ('B', 'Y'): 5,  # paper, paper -> (2 + 3 = 5)
        ('B', 'Z'): 9,  # paper, scissors -> (3 + 6 = 9)
        ('C', 'X'): 7,  # scissors, rock -> (1 + 6 = 7)
        ('C', 'Y'): 2,  # scissors, paper -> (2 + 0 = 2)
        ('C', 'Z'): 6}  # scissors, scissors -> (3 + 3 = 6)

    for line in file:
        line = line.rstrip().split()
        round_points = round_value[(line[0], line[1])]
        points_total += round_points

    return points_total
