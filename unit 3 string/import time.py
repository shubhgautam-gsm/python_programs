import time

def simulate_task():
    total_steps = 10
    for i in range(total_steps + 1):
        progress = i / total_steps
        print(f"Progress: [{'=' * i}{' ' * (total_steps - i)}] {progress * 100:.2f}%", end='\r')
        time.sleep(0.5)  # Simulating some work

simulate_task()
print("\nTask complete!")
