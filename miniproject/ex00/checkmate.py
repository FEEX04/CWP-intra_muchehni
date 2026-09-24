#!/usr/bin/env python3

def checkmate(board):                                             #ประกาศสร้างฟังก์ชันชื่อ checkmate โดยรับพารามิเตอร์ชื่อ board (กระดานหมากรุกที่ส่งเข้ามา)
    if not isinstance(board, str) or not board:
        return

    # แยกบรรทัดและกรองบรรทัดว่างออก
    lines = [line for line in board.splitlines() if line]
    if not lines:
        return

    # ตรวจสอบว่าเป็นกระดานสี่เหลี่ยมจัตุรัส (N x N)
    n = len(lines)
    for line in lines:
        if len(line) != n:
            return

    # ค้นหาตำแหน่ง King (ต้องมี K เพียง 1 ตัวเท่านั้น)
    king_pos = None
    king_count = 0
    for r in range(n):
        for c in range(n):
            if lines[r][c] == 'K':
                king_pos = (r, c)
                king_count += 1

    if king_count != 1:
        return

    kr, kc = king_pos

    # 1. เช็กแนวตั้งและแนวนอน (Rook, Queen)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            ch = lines[r][c]
            if ch in ('P', 'B', 'R', 'Q', 'K'):
                if ch in ('R', 'Q'):
                    print("Success")
                    return
                break  # ถูกหมากตัวอื่นบัง
            r += dr
            c += dc

    # 2. เช็กแนวเฉียงขึ้นบน (Bishop, Queen)
    for dr, dc in [(-1, -1), (-1, 1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            ch = lines[r][c]
            if ch in ('P', 'B', 'R', 'Q', 'K'):
                if ch in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc

    # 3. เช็กแนวเฉียงลงล่าง (Pawn ที่ระยะ 1 ช่อง, Bishop, Queen)
    for dr, dc in [(1, -1), (1, 1)]:
        r, c = kr + dr, kc + dc
        dist = 1
        while 0 <= r < n and 0 <= c < n:
            ch = lines[r][c]
            if ch in ('P', 'B', 'R', 'Q', 'K'):
                if dist == 1 and ch in ('P', 'B', 'Q'):
                    print("Success")
                    return
                elif dist > 1 and ch in ('B', 'Q'):
                    print("Success")
                    return
                break
            r += dr
            c += dc
            dist += 1

    print("Fail")
