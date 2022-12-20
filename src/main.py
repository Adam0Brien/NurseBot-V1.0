import multiprocessing
import subprocess

def run_script(script_path):
    # Use subprocess to run the script
    subprocess.run(["python3", script_path])

# Create a list of the scripts that you want to run
scripts = ["heartbeat.py", "sound.py","tempH.py"]

# Create a list of processes
processes = []

# Start a process for each script
for script in scripts:
    p = multiprocessing.Process(target=run_script, args=(script,))
    p.start()
    processes.append(p)

# Wait for all processes to complete
for p in processes:
    p.join()

print("All scripts have finished running.")
