import pyautogui
import time

print("Move your mouse to the desired position. Press Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        position_str = f'X: {x} Y: {y}'
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone.")
