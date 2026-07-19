import time

def audit_quantum_output(result: int) -> bool:
    print("[AUDIT] Initiating 3-tier safety check on calculation product...")
    time.sleep(0.5)
    
    if result < 3 or result > 5:
        return False
        
    if bin(result) != '0b100':
        return False
        
    if (result - 2) != 2:
        return False
        
    print("[AUDIT] Product verified. Result is structurally sound.")
    return True