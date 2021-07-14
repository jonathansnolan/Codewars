def get_count(input_str):
    vowels = ["a", "e", "i", "o", "u"]
    x = list(input_str)

    num_vowels = 0

    for k in x:
        for j in vowels:
            if k == j:
                num_vowels += 1
            else:
                num_vowels += 0
