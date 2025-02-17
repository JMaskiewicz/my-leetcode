from collections import defaultdict

# Input Data
num_players = 8
players = [(-10, -10), (-10, 10), (0, -10), (0, 10), (10, -10), (10, 10), (-9, -10), (-9, 0)]

from collections import defaultdict

def preprocess_throws(players):
    vertical, horizontal = defaultdict(list), defaultdict(list)
    diagonal1, diagonal2 = defaultdict(list), defaultdict(list)

    for idx, (x, y) in enumerate(players):
        player_number = idx + 1  # 1-based index

        # Store players by vertical and horizontal alignment
        vertical[x].append((x, y, player_number))  # Sorted by y
        horizontal[y].append((x, y, player_number))  # Sorted by x

        # Correct diagonal calculations
        b1 = y - x  # Main diagonal (↘ `/`)
        b2 = y + x  # Anti-diagonal (↙ `\`)

        diagonal1[b1].append((x, y, player_number))
        diagonal2[b2].append((x, y, player_number))

    # Sort players in each group for fast nearest-neighbor lookup
    for d in [vertical, horizontal, diagonal1, diagonal2]:
        for key in d:
            d[key].sort()

    return vertical, horizontal, diagonal1, diagonal2




# Process players
vertical, horizontal, diagonal1, diagonal2 = preprocess_throws(players)

# Print results
print("Vertical:", dict(vertical))
print("Horizontal:", dict(horizontal))
print("Diagonal 1:", dict(diagonal1))
print("Diagonal 2:", dict(diagonal2))
