import random
QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("It always seems impossible until it's done.", "Nelson Mandela"),
    ("Whether you think you can or you think you can't, you're right.", "Henry Ford"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("Don't watch the clock; do what it does. Keep going.", "Sam Levenson"),
    ("You miss 100% of the shots you don't take.", "Wayne Gretzky"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The future belongs to those who believe in the beauty of their dreams.", "Eleanor Roosevelt"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Be yourself; everyone else is already taken.", "Oscar Wilde"),
    ("In the middle of every difficulty lies opportunity.", "Albert Einstein"),
    ("What we think, we become.", "Buddha"),
]
def main() -> None:
    quote, author = random.choice(QUOTES)
    print(f'"{quote}" — {author}')
if __name__ == "__main__":
    main()