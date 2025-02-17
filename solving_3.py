from collections import defaultdict

def preprocess_throws(players):
    vertical, horizontal = defaultdict(list), defaultdict(list)
    diagonal1, diagonal2 = defaultdict(list), defaultdict(list)

    for idx, (x, y) in enumerate(players):
        player_number = idx + 1  # 1-based index

        # Store players by vertical and horizontal alignment
        vertical[x].append((y, player_number))  # Sorted by y
        horizontal[y].append((x, player_number))  # Sorted by x

        b1 = y - x  # Line equation y = x - b
        b2 = y + x  # Line equation y = x + b

        diagonal1[b1].append((x, player_number))
        diagonal2[b2].append((x, player_number))

    # Sort players in each group for fast nearest-neighbor lookup
    for d in [vertical, horizontal, diagonal1, diagonal2]:
        for key in d:
            d[key].sort()

    return vertical, horizontal, diagonal1, diagonal2

DIRECTION_VECTORS = {
    "N": (0, 1), "NE": (1, 1), "E": (1, 0), "SE": (1, -1),
    "S": (0, -1), "SW": (-1, -1), "W": (-1, 0), "NW": (-1, 1)
}

def get_next_direction(received_from):
    direction_order = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    return direction_order[(direction_order.index(received_from) + 1) % 8]

from bisect import bisect_right, bisect_left

def find_next_player(current_pos, direction, players, storage):
    x, y = current_pos

    # Determine the relevant dictionary based on direction
    if direction in ["N", "S"]:
        axis_dict = storage[0]
        key, val = x, y
        search_forward = direction == "N"
    elif direction in ["E", "W"]:
        axis_dict = storage[1]
        key, val = y, x
        search_forward = direction == "E"
    elif direction in ["NE", "SW"]:
        axis_dict = storage[2]
        key, val = y - x, x
        search_forward = direction == "NE"
    else:  # NW, SE
        axis_dict = storage[3]
        key, val = y + x, x
        search_forward = direction == "NW"

    if key not in axis_dict:
        return None, None

    positions = axis_dict[key]  # Sorted list of (coordinate, player_index)

    # Use binary search to locate the next player
    pos_list = [p[0] for p in positions]  # Extract sorted positions
    index = bisect_right(pos_list, val) if search_forward else bisect_left(pos_list, val) - 1

    # Ensure we are within bounds and the player is active
    while 0 <= index < len(positions):
        next_pos, next_player = positions[index]
        if next_player in players:
            return next_player, players[next_player]
        index += 1 if search_forward else -1  # Move in the correct direction

    return None, None  # No valid player found


def simulate_game(n, players, start_dir, start_idx, storage):
    if start_idx not in range(1, n + 1):
        print("Invalid starting player number!")
        return

    current_player = start_idx
    current_pos = players[current_player - 1]  # 1-based index correction
    received_from = start_dir
    throw_count = 0

    print(f"Start: Player {current_player} at {current_pos} receives the ball from {start_dir}")

    active_players = {i + 1: players[i] for i in range(n)}
    active_players.pop(current_player)

    while True:
        found_next = False
        next_dir = get_next_direction(received_from)

        for _ in range(8):
            next_player, next_pos = find_next_player(current_pos, next_dir, active_players, storage)

            if next_player is not None:
                throw_count += 1
                print(
                    f"Throw {throw_count}: Player {current_player} throws to Player {next_player} ({next_pos}) in direction {next_dir}")
                received_from = next_dir
                current_player = next_player
                current_pos = next_pos
                active_players.pop(next_player)
                found_next = True
                break

            next_dir = get_next_direction(next_dir)  # Rotate clockwise

        if not found_next:
            break

    print(f"Game ends. Total throws: {throw_count}, Last player: {current_player}")
    return throw_count, current_player

# Example Input
test_players = [(-100, -100), (-100, 100), (0, -100), (0, 100), (100, -100), (100, 100), (-99, -100), (-99, 0)]
storage = preprocess_throws(test_players)

num_players = len(test_players)
starting_direction = "SE"
starting_player = 4

simulate_game(num_players, test_players, starting_direction, starting_player, storage)
