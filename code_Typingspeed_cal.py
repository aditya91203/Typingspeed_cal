import time
import random

# List of sentences to type
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language.",
    "Typing speed tests are fun and useful.",
    "Practice makes perfect in any skill.",
    "Artificial intelligence is transforming the world."
]

def typing_speed_test():
    # Select a random sentence
    sentence = random.choice(sentences)
    
    print("Type the following sentence as fast as you can:")
    print(sentence)
    
    # Start the timer
    start_time = time.time()
    
    # Get user input
    user_input = input("Start typing: ")
    
    # End the timer
    end_time = time.time()
    
    # Calculate the time taken
    time_taken = end_time - start_time
    
    # Calculate typing speed in words per minute (WPM)
    words_typed = len(user_input.split())
    wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0
    
    # Check for accuracy
    accuracy = (sum(1 for a, b in zip(user_input, sentence) if a == b) / len(sentence)) * 100
    
    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")
    
# Run the typing speed test
typing_speed_test()
