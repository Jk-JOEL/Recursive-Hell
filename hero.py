import random

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
            print(f">>> ERROR: Identity Corruption... New ID: {new_name}")

        if new_integrity == 0:
            # The Singularity
            print(f"\n[VOICE_LOG]: {new_name} says: 'I am... becoming a constant.'")
            return Hero(new_name, 0)
            
        return Hero(new_name, new_integrity)


hero = Hero("Hermit", 100)
hero = hero - 60
print(hero)
