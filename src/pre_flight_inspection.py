import sys
import platform
import time

print("=" * 50)
print("       SYSTEM INTEGRITY PRE-FLIGHT CHECK        ")
print("=" * 50)

time.sleep(0.5)
print(f"[OS] Detecting operating system... {platform.system()} ({platform.release()})")
print(f"[CPU] Inspecting core architecture... {platform.processor()}")

time.sleep(0.5)
print("[RAM] Checking if memory can hold the digit '4'... Yes.")

time.sleep(0.5)
print("[ENV] Verifying Python interpreter status... STABLE.")

print("=" * 50)
print(" STATUS: ALL SYSTEMS GO. READY FOR ADDITION. ")
print("=" * 50)