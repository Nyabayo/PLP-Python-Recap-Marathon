# Random Joke Generator 🤣
# Build a program that stores a list of jokes and randomly selects one to display every time the user runs it. Add a fun twist with jokes about Python or programming! 🐍💡
import random

# List of jokes about Python and programming
jokes = [
    "Why do programmers prefer dark mode? Because the light attracts bugs! 🐞",
    "Why did the Python programmer break up with their partner? They couldn't handle the exceptions. 💔",
    "What do you call 8 hobbits? A hobbyte. 😄",
    "Why do Java developers wear glasses? Because they don't see sharp. 👓",
    "Why can't Python play poker? It can't deal with the exceptions. 😂",
    "What is a programmer's favorite hangout place? The Foo Bar. 🍻",
    "Why was the JavaScript developer sad? Because they didn't know how to 'null' their feelings. 😞",
    "How do you comfort a JavaScript bug? You console it. 🖥️"
]

# Randomly select a joke from the list
random_joke = random.choice(jokes)

# Display the selected joke
print(random_joke)
