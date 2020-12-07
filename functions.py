import re


class TurkishCharacter:
    def __init__(self):
        pass

    @staticmethod
    def tr_upper(word):
        word = re.sub(r"i", "İ", word)
        word = re.sub(r"ı", "I", word)
        word = re.sub(r"ç", "Ç", word)
        word = re.sub(r"ş", "Ş", word)
        word = re.sub(r"ü", "Ü", word)
        word = re.sub(r"ğ", "Ğ", word)
        word = word.upper()  # for the rest use default upper
        return word

    @staticmethod
    def tr_lower(word):
        word = re.sub(r"İ", "i", word)
        word = re.sub(r"I", "ı", word)
        word = re.sub(r"Ç", "ç", word)
        word = re.sub(r"Ş", "ş", word)
        word = re.sub(r"Ü", "ü", word)
        word = re.sub(r"Ğ", "ğ", word)
        word = word.lower()  # for the rest use default lower
        return word

    @staticmethod
    def tr_capitalize(param_word):
        if param_word != "" and not str(param_word).isspace():
            word_list = param_word.split(sep=" ")
            new_word = ""
            for word in word_list:
                first_letter = word[0]
                last_part = word[1:]

                first_letter = re.sub(r"i", "İ", first_letter)
                first_letter = re.sub(r"ı", "I", first_letter)
                first_letter = re.sub(r"ç", "Ç", first_letter)
                first_letter = re.sub(r"ş", "Ş", first_letter)
                first_letter = re.sub(r"ü", "Ü", first_letter)
                first_letter = re.sub(r"ğ", "Ğ", first_letter)

                last_part = re.sub(r"İ", "i", last_part)
                last_part = re.sub(r"I", "ı", last_part)
                last_part = re.sub(r"Ç", "ç", last_part)
                last_part = re.sub(r"Ş", "ş", last_part)
                last_part = re.sub(r"Ü", "ü", last_part)
                last_part = re.sub(r"Ğ", "ğ", last_part)

                rebuilt_word = first_letter + last_part
                rebuilt_word = rebuilt_word.capitalize()
                new_word = new_word + " " + rebuilt_word

            new_word = new_word.strip()
            return new_word
        return ""

