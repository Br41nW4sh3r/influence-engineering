# [B4W] Bias Detector
# Detect manipulation patterns in text
# Usage: python3 bias-detector.py "Buy now, only today, everyone is doing it!"

import sys
import re

PATTERNS = {
    "URGENCY": [r"only today", r"last chance", r"now or never", r"limited time", r"hurry", r"act now"],
    "SOCIAL PROOF": [r"everyone", r"millions", r"everybody", r"all people", r"trending"],
    "AUTHORITY": [r"experts say", r"scientists prove", r"studies show", r"doctor", r"official"],
    "FEAR": [r"you will lose", r"danger", r"warning", r"don't miss", r"you are being", r"threat"],
    "SCARCITY": [r"only \d+ left", r"sold out", r"almost gone", r"exclusive", r"secret"],
}

def analyze(text):
    text_low = text.lower()
    found = []
    score = 0
    print(f"\n[ B4W ] Analyzing: \"{text}\"\n")
    print("-" * 50)
    for category, patterns in PATTERNS.items():
        for p in patterns:
            if re.search(p, text_low):
                print(f"[!] {category} detected: '{p}'")
                found.append(category)
                score += 20
                break
    
    print("-" * 50)
    print(f"Manipulation Score: {min(score, 100)}/100")
    
    if score == 0:
        print("Result: CLEAN - No obvious patterns.")
    elif score < 40:
        print("Result: LOW - Stay alert.")
    elif score < 80:
        print("Result: MEDIUM - Probably trying to persuade you.")
    else:
        print("Result: HIGH - Classic Persuasion Stack detected. Pause.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python3 bias-detector.py "your text here"')
    else:
        analyze(" ".join(sys.argv[1:]))
