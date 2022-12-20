import multiprocessing
import subprocess

def run_script(script_path):
    # Use subprocess to run the script
    subprocess.run(["python3", script_path])

scripts = ["heartbeat.py", "sound.py","bme680data.py"]

processes = []

for script in scripts:
    p = multiprocessing.Process(target=run_script, args=(script,))
    p.start()
    processes.append(p)

for p in processes:
    p.join()

print("All scripts have finished running.")
