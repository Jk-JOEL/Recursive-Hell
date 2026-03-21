import random
import time
import sys # Using later

class Hero:
    def __init__(self, name, integrity):
        self.name = name
        self.integrity = integrity

    def __repr__(self):
        return f"Hero(name='{self.name}', integrity={self.integrity})"

    def __sub__(self, amount):
        # abs() ensures we ALWAYS subtract, even if input is negative
        clean_amount = abs(amount)
        new_integrity = max(0, self.integrity - clean_amount)
        new_name = self.name
        
        # IDENTITY GLITCH: Triggers between 1 and 49 integrity
        if 0 < new_integrity < 50:
            
            if len(self.name) <= 1:
                # Replace single char with 3 random symbols
                new_name = "".join([random.choice("!@#$%^&*") for _ in range(3)])
            else:
                # Scramble existing name
                char_list = list(self.name)
                random.shuffle(char_list)
                new_name = "".join(char_list)

        if new_integrity == 0:
            # The Singularity
            print(f"\n[VOICE_LOG]: {new_name} says: 'I am... becoming a constant.'")
            return Hero(new_name, 0)
            
        return Hero(new_name, new_integrity)


hero = Hero("Hermit", 250)

bpm = 170.00 
counter = 0

import time
import random
import sys

# --- SETTINGS ---
bpm_delay = 0.35  # 170 BPM
beat_count = 0

while hero.integrity > 0:
    time.sleep(bpm_delay)
    beat_count += 1
    
    # EVERY 4TH BEAT: Trigger the Identity Glitch
    if beat_count % 4 == 0:
        # Subtracting 5 instead of 1 to speed up the decay on the snare
        hero = hero - 5
        print(f"[SNARE HIT] {hero}")
    else:
        # Normal steady decay on the other beats
        hero = hero - 1
        print(f" (kick)   {hero.integrity}")
    sys.stdout.flush()

print("\n--- SYSTEM HALTED: SINGULARITY REACHED ---")
    
