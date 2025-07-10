import tkinter as tk
from transformers import pipeline

# Load the zero-shot classification pipeline
zero_shot_classifier = pipeline(
    "zero-shot-classification", model="facebook/bart-large-mnli"
)

# Global state for pagination
results = []
page_index = 0
page_size = 3

# Create Tkinter window
root = tk.Tk()
root.title("Zero-Shot Classifier")

# Function to display classification results
def display_results():
    global page_index
    start = page_index * page_size
    end = start + page_size
    subset = results[start:end]

    if not subset:
        result_label.config(text="No more results.")
        return

    # Sort by score descending
    sorted_subset = sorted(subset, key=lambda x: x[1], reverse=True)

    lines = []
    for i, (label, score) in enumerate(sorted_subset):
        if i == 0:
            lines.append(f"✅ Likely related to **{label}** (score: {score:.2f})")
        elif i == len(sorted_subset) - 1:
            lines.append(f"❌ Highly unrelated to **{label}** (score: {score:.2f})")
        else:
            lines.append(f"• Possibly related to {label} (score: {score:.2f})")

    result_label.config(text="\n\n".join(lines))

# Function to classify input text
def classify_text():
    global results, page_index
    sequence = input_sequence.get().strip()
    labels = input_labels.get().strip()

    if not sequence or not labels:
        result_label.config(text="Please enter both a sentence and candidate labels.")
        return

    candidate_labels = [label.strip() for label in labels.split(",") if label.strip()]
    output = zero_shot_classifier(sequence, candidate_labels)

    results = list(zip(output["labels"], output["scores"]))
    page_index = 0
    display_results()

# Function to go to next page
def next_page():
    global page_index
    page_index += 1
    display_results()

# UI Elements
tk.Label(root, text="Enter a sentence:", font=("Arial", 14)).pack(pady=(10, 0))
input_sequence = tk.Entry(root, width=60, font=("Arial", 12))
input_sequence.pack(pady=5)

tk.Label(root, text="Enter candidate labels (comma-separated):", font=("Arial", 14)).pack(pady=(10, 0))
input_labels = tk.Entry(root, width=60, font=("Arial", 12))
input_labels.pack(pady=5)

tk.Button(root, text="Classify", font=("Arial", 12), command=classify_text).pack(pady=5)
tk.Button(root, text="Next", font=("Arial", 12), command=next_page).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=600, justify="left")
result_label.pack(pady=10, padx=15)

# Launch app
root.mainloop()
