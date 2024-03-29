def task4():
    # The original text string
    text = (
        "So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy and stupid, "
        "whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, "
        "when suddenly a White Rabbit with pink eyes ran close by her."
    )

    # Task a) Determine the number of lowercase letters
    # Count each character in the text that is a lowercase letter
    lowercase_count = sum(1 for char in text if char.islower())
    print(f"a)a)Number of lowercase letters: {lowercase_count}")

    # Task b) Find the last word containing the letter 'i' and its number
    # Split the text into words and enumerate them starting from 1
    words = text.split()
    last_i_word = None  # Initialize the variable to store the last word with 'i'
    last_i_index = None  # Initialize the variable to store the index of the last word with 'i'
    # Iterate through the words and their indices
    for index, word in enumerate(words, start=1):
        # Check if the word contains the letter 'i'
        if 'i' in word.lower():
            last_i_word = word  # Update the last word with 'i'
            last_i_index = index  # Update the index of the last word with 'i'
    print(f"b)The last word with the letter 'i': {last_i_word}, its number: {last_i_index}")

    # Task c) Output the string excluding words starting with 'i'
    # Join words that do not start with 'i' into a new string
    filtered_text = ' '.join(word for word in words if not word.lower().startswith('i'))
    print(f"c)A string without words starting with 'i': {filtered_text}")
