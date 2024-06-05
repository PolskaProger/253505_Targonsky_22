def safe_input(prompt, expected_type):
    while True:
        try:
            return expected_type(input(prompt))
        except ValueError:
            print(f"Input of the {expected_type.__name__} type is expected. Try again.")