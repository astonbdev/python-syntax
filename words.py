def print_upper_words(words, must_start_with):
    for letter in must_start_with:
        for word in words:
            if word.startswith(f"{letter.upper()}") or word.startswith(f"{letter.lower()}"):
                upper = word.upper()
                print(upper)

print_upper_words(["hello", "jason", "macaroni","edwin", "Electric"], {"y", "m", "e"})