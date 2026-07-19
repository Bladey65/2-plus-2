import sys

PRIMARY_FACTOR: int = 2
SECONDARY_FACTOR: int = 2

if PRIMARY_FACTOR != SECONDARY_FACTOR:
    print("[CRITICAL] Fundamental mathematical asymmetry detected.")
    sys.exit(500)