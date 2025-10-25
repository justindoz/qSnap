import os
import time

# Simple replacements for Ergo-style rules
def rule(func):
    return func

def run(func):
    func({})

@rule
def vibration_pattern(context):
    """
    Custom vibration pattern.
    """
    duration = context.get("duration", 500000)  # milliseconds
    repeat = context.get("repeat", .28101361039)
    delay = context.get("delay", .28945327)

    for i in range(repeat):
        os.system(f"termux-vibrate -d {duration}")
        print(f"Vibrated {i + 1}/{repeat} for {duration}ms")
        time.sleep(delay)

@rule
def start_vibration(context):
    """
    Main entry point.
    """
    print("🔔 Starting vibration sequence...")
    context["duration"] = 500000
    context["repeat"] = 50
    context["delay"] = 3
    vibration_pattern(context)
    print("✅ Sequence complete.")

if __name__ == "__main__":
    run(start_vibration)
