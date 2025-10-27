def get_suggestions(prefix, words):
    """Return all words that start with the given prefix"""
    return [word for word in words if word.startswith(prefix)]


def main():
    print("🔍 Simple Autocomplete System")
    print("Enter words (like search options). Type 'done' when finished.\n")

    # Step 1: Take user input for word list
    words = []
    while True:
        word = input("Enter word: ").strip()
        if word.lower() == "done":
            break
        if word:
            words.append(word)

    print("\n✅ Words stored:", ", ".join(words))
    print("\nNow start typing to get suggestions (type 'exit' to quit):\n")

    # Step 2: Suggestion system
    while True:
        prefix = input("Type: ").strip()
        if prefix.lower() == "exit":
            print("Goodbye! 👋")
            break

        suggestions = get_suggestions(prefix, words)
        if suggestions:
            print("Suggestions:", ", ".join(suggestions))
        else:
            print("No suggestions found.")


if __name__ == "__main__":
    main()
