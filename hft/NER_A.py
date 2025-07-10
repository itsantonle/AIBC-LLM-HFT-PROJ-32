import tkinter as tk
from transformers import pipeline

# Load the NER pipeline
ner_pipeline = pipeline("ner", model="dslim/bert-base-NER", grouped_entities=True)

# Explanation for common entity tags lol i just pull this from the internet
ENTITY_EXPLANATIONS = {
    "PER": "Person (e.g., John, Mary)",
    "LOC": "Location (e.g., Paris, New York)",
    "ORG": "Organization (e.g., Microsoft, UN)",
    "MISC": "Miscellaneous (e.g., events, nationalities)"
}

#tkinter 
root = tk.Tk()
root.title("Named Entity Recognizer")


entities = []
page_index = 0
page_size = 3


def display_entities():
    global page_index
    start = page_index * page_size
    end = start + page_size
    subset = entities[start:end]

    if not subset:
        result_label.config(text="No more entities.")
        return

    lines = []
    for ent in subset:
        word = ent['word']
        label = ent['entity_group']
        score = f"{ent['score']:.2f}"
        explanation = ENTITY_EXPLANATIONS.get(label, "No explanation available.")
        lines.append(f"{word} ({label}, score: {score})\n→ {explanation}")

    result_label.config(text="\n\n".join(lines))

# analyze_
def analyze_text():
    global entities, page_index
    text = input_field.get().strip()
    if not text:
        result_label.config(text="Please enter some text.")
        return

    entities = ner_pipeline(text)
    page_index = 0
    display_entities()


def next_page():
    global page_index
    page_index += 1
    display_entities()

# UI Elements
tk.Label(root, text="Enter text for NER:", font=("Arial", 14)).pack(pady=(10, 5))

input_field = tk.Entry(root, width=60, font=("Arial", 12))
input_field.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze", font=("Arial", 12), command=analyze_text)
analyze_button.pack(pady=5)

next_button = tk.Button(root, text="Next", font=("Arial", 12), command=next_page)
next_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=600, justify="left")
result_label.pack(pady=10, padx=15)


root.mainloop()
