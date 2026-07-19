import sys
import time

print("\n!!! EMERGENCY PARADOX DETECTED !!!")
print("Initiating full system dump to prevent CPU meltdown...")

for percent in range(0, 101, 25):
    print(f"[ABORT] Purging memory registers... {percent}%")
    time.sleep(0.4)

print("[SUCCESS] Core cooled down. Math successfully prevented.")
sys.exit(0)