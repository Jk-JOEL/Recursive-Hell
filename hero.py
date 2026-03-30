import random
import time
import sys
from datetime import datetime

def log_print(msg):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] {msg}")

class Hero:
    
    def __init__(self, name, integrity=100):
        self.name = name
        self.integrity = integrity
        self.beats_survived = 0

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


# Only Positive Integers
hero = Hero("Hermit", 150)
# Settings for the bar
bar_max_width = 20
total_start_integrity = hero.integrity 
beat_count = 0
# Dynamic Delays (seconds)
min_d = 0.225 
max_d = 0.350

# Glitchy Beats
current_ratio = round(hero.integrity / total_start_integrity * 1.45) 
dynamic_delay = min_d + (max_d - min_d) * current_ratio

time.sleep(dynamic_delay)

print("Starting...") # Just making sure it's synced right on my end

while hero.integrity > 0:

    ACTIONS = ["Deflecting border...", "Internalizing doubt...", "Processing memories...", "Scanning world..."]

    print("\n")
    
    current_ratio = round(hero.integrity / total_start_integrity * 1.45)
    dynamic_delay = min_d + (max_d - min_d) * current_ratio

    time.sleep(dynamic_delay)

    beat_count = (beat_count % 4) + 1
    
    fill_count = int((hero.integrity / total_start_integrity) * bar_max_width)
    bar = "█" * fill_count + "░" * (bar_max_width - fill_count)
    
    jitter = " " * random.randint(0, 8)
    
    if beat_count == 4: # If Wall (AHHHHHHHH!!!)
        hero = hero - 8
        log_print(f"{jitter}[{bar}] SNARE! -> {hero.name}")
    elif beat_count == 2:
        action = random.choice(ACTIONS)
        log_print(f" >> [ACTION]: {action}")
    else:
        hero = hero - 2
        log_print(f"{jitter}[{bar}] kick")
        
    hero.beats_survived += 1
    
    sys.stdout.flush()



print(f"\nHero Lifespan: {random.randint(3,10)} Months.") # Completely arbitary, not sure about the lore yet.
print("Solving...\n")
time.sleep(2.5)

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
print(singularity_art)
sys.stdout.flush() # Online Python - IDE, Editor, Compiler, Interpreter      
