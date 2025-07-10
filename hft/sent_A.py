import tkinter as tk
from transformers import pipeline
import nltk
from collections import Counter
import threading

# nltk package setup
def download_nltk_resources():
    nltk.download("punkt", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)

# POS extraction 
def extract_pos(text):
    try:
        tokens = nltk.word_tokenize(text)
        tagged = nltk.pos_tag(tokens)

        verbs = [word.lower() for word, pos in tagged if pos.startswith("VB")]
        adjs = [word.lower() for word, pos in tagged if pos.startswith("JJ")]

        verb = Counter(verbs).most_common(1)
        adj = Counter(adjs).most_common(1)

        top_verb = verb[0][0] if verb else "None"
        top_adj = adj[0][0] if adj else "None"

        return top_verb, top_adj, None  
    except Exception as e:
        return None, None, str(e)  

# use the distilbert model for sentiment analysis
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0"
)

# tkinter
root = tk.Tk()
root.title("Sentiment + POS Analyzer")

# Analysis function
def analyze_text():
    text = input_field.get().strip()
    if not text:
        emoji_label.config(text="❓", font=("Arial", 60))
        pos_label.config(text="Please enter a sentence.")
        return

    # Sentiment analysis
    result = classifier(text)[0]
    label = result['label']

    emoji = "😄" if label == "POSITIVE" else "🥲"
    emoji_label.config(text=emoji, font=("Arial", 100))

    # POS analysis
    verb, adj, error = extract_pos(text)

    if error:
        pos_label.config(text=f"POS tagging error: {error}")
    elif verb == "None" and adj == "None":
        pos_label.config(text="No verbs or adjectives found.")
    else:
        pos_label.config(text=f"Top Verb: {verb}    |    Top Adjective: {adj}")

# UI Elements
tk.Label(root, text="Enter a sentence:", font=("Arial", 16)).pack(pady=(15, 5), padx=15)

input_field = tk.Entry(root, width=60, font=("Arial", 14))
input_field.pack(pady=5, padx=15)

run_button = tk.Button(root, text="Analyze", font=("Arial", 14), command=analyze_text)
run_button.pack(pady=10, padx=15)

emoji_label = tk.Label(root, text="", font=("Arial", 40))
emoji_label.pack(pady=10, padx=15)

pos_label = tk.Label(root, text="POS results will appear here.", font=("Arial", 16), wraplength=600, justify="center")
pos_label.pack(pady=10, padx=15)

# thread to download NLTK resources
threading.Thread(target=download_nltk_resources).start()


root.mainloop()
