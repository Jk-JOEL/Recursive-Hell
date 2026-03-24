import random
import time
import sys

class Hero:
    def __init__(self, name, integrity):
        self.name = name
        self.integrity = integrity

    def __repr__(self):
        return f"ID:{self.name} | INT:{self.integrity}"

    def __sub__(self, amount):
        clean_amount = abs(amount)
        new_integrity = max(0, self.integrity - clean_amount)
        new_name = self.name
        
        if 0 < new_integrity < 50:
            char_list = list(self.name)
            if random.random() < 0.3:
                char_list.append(random.choice("!@#$%^&*░▒▓"))
            random.shuffle(char_list)
            new_name = "".join(char_list)[:10]

        if new_integrity == 0:
            print(f"\n[VOICE_LOG]: {new_name} -> 'CONSTANT REACHED.'")
            return Hero(new_name, 0)
            
        return Hero(new_name, new_integrity)

hero = Hero("Hermit", 150)
# Settings for the bar
bar_max_width = 20
total_start_integrity = hero.integrity 
beat_count = 0
bpm_delay = round(60.00 / 170.00, 2)

print("Starting...") # Just making sure it's synced right on my end

while hero.integrity > 0:
    time.sleep(bpm_delay)
    beat_count = (beat_count % 4) + 1
    
    # 1. Calculate bar fill
    # Using 'int' to keep it to whole blocks
    fill_count = int((hero.integrity / total_start_integrity) * bar_max_width)
    bar = "█" * fill_count + "░" * (bar_max_width - fill_count)
    
    # 2. Add Jitter for that glitch feel
    jitter = " " * random.randint(0, 8)
    
    # 3. Execution
    print("/n")
    if beat_count == 4:
        hero = hero - 8
        print(f"{jitter}[{bar}] SNARE! -> {hero.name}")
    else:
        hero = hero - 2
        print(f"{jitter}[{bar}] kick")
        
    sys.stdout.flush()

# The System Crash Visual
singularity_art = """
[ ! ] ERROR: CORE_INTEGRITY_FAILURE
[ ! ] IDENTITY: 0% 
[ ! ] RECURSIVE LOOP TERMINATED
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░█▀█░█▀█░█▀█░█▀█░█▀█░█▀█░█▀█░░
░░█▄█░█▄█░█▄█░█▄█░█▄█░█▄█░█▄█░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
[ ! ] STATUS: BECOMING A CONSTANT.
"""
time.sleep(1) # Dramatic pause before the crash
print(singularity_art)
sys.stdout.flush()# Online Python - IDE, Editor, Compiler, Interpreter

    
