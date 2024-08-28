def count_elements(sentence):
    words = len(sentence.split())
    digits = sum(c.isdigit() for c in sentence)
    uppercase = sum(c.isupper() for c in sentence)
    lowercase = sum(c.islower() for c in sentence)

    print(f"This sentence has {words} words")
    print(f"This sentence has {digits} digits")
    print(f"{uppercase} upper case letters")
    print(f"{lowercase} lower case letters")

sentence = input("Enter a sentence: ")
count_elements(sentence)
