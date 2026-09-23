def checkmate(board: str) -> None:
    if not isinstance(board, str):
        return

    lines = board.splitlines()
    if not lines:
        return

    size = len(lines)
    if any(len(line) != size for line in lines):
        return

    king_pos = None
    king_count = 0

    for r in range(size):
        for c in range(size):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1 or king_pos is None:
        return

    kr, kc = king_pos

    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            char = lines[r][c]
            if char in ('R', 'Q'):
                print("Success")
                return
            elif char in ('P', 'B', 'K'):
                break
            r += dr
            c += dc

    up_diag_dirs = [(-1, -1), (-1, 1)]
    for dr, dc in up_diag_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            char = lines[r][c]
            if char in ('B', 'Q'):
                print("Success")
                return
            elif char in ('P', 'R', 'K'):
                break
            r += dr
            c += dc

    down_diag_dirs = [(1, -1), (1, 1)]
    for dr, dc in down_diag_dirs:
        r, c = kr + dr, kc + dc
        step = 1
        while 0 <= r < size and 0 <= c < size:
            char = lines[r][c]
            if char in ('B', 'Q'):
                print("Success")
                return
            elif char == 'P':
                if step == 1:
                    print("Success")
                    return
                else:
                    break
            elif char in ('R', 'K'):
                break
            r += dr
            c += dc
            step += 1

    print("Fail")