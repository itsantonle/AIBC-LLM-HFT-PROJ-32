import tkinter as tk
import subprocess
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Launch a script
def launch_script(script_name):

    status_label.config(text="Launching tool, please wait...")
    root.update_idletasks()  


    script_path = os.path.join(BASE_DIR, script_name)
    subprocess.Popen(["python", script_path])


    root.after(2000, lambda: status_label.config(text=""))

# Create main window
root = tk.Tk()
root.title("AI Toolkit Launcher")

tk.Label(root, text="Choose a tool to launch:", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Named Entity Recognizer", font=("Arial", 14),
          command=lambda: launch_script("NER_A.py")).pack(pady=10)

tk.Button(root, text="Sentiment + POS Analyzer", font=("Arial", 14),
          command=lambda: launch_script("sent_A.py")).pack(pady=10)

tk.Button(root, text="Zero-Shot Classifier", font=("Arial", 14),
          command=lambda: launch_script("zeroS_A.py")).pack(pady=10)


status_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
status_label.pack(pady=15)

root.mainloop()
