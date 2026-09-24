#!/usr/bin/env python3

import sys
from checkmate import checkmate

def main():
    # 1. เช็กว่ามีการส่งชื่อไฟล์มาจาก Terminal หรือไม่
    if len(sys.argv) < 2:
        return

    # 2. วนลูปอ่านทีละไฟล์ (กรณีใส่หลายไฟล์พร้อมกัน)
    for file_path in sys.argv[1:]:
        try:
            with open(file_path, 'r') as file:
                board = file.read()
                checkmate(board)
        except Exception:
            # ถ้าเปิดไฟล์ไม่ได้/หาไฟล์ไม่เจอ ให้ข้ามอย่างปลอดภัย ไม่ให้โปรแกรม Crash
            continue

if __name__ == "__main__":
    main()
