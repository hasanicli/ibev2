import locale
import re
person_dict = dict()


def get_list_personal(p_data):
    person_dict.clear()
    recorded_item = []
    for number, item in enumerate(p_data):
        person_dict[number] = item
        recorded_item.append(item[0] + " " + item[1] + " " + str(number))
    recorded_item.sort(key=locale.strxfrm)
    return recorded_item


def get_list_general(p_data):
    recorded_item = []
    for item in p_data:
        recorded_item.append(item[0])
    recorded_item.sort(key=locale.strxfrm)
    return recorded_item


def find_id_number(p_text):
    text_list = p_text.split()
    index = int(text_list[len(text_list) - 1])
    person_list = person_dict[index]
    return person_list[2]


def find_id_numbers(p_obj):
    id_numbers = []
    for item in [p_obj.item(index) for index in range(p_obj.count())]:
        item_list = item.text().split()
        index = int(item_list[len(item_list) - 1])
        person_list = person_dict[index]
        id_numbers.append(person_list[2])
    return id_numbers


def stripper(p_text):
    word_list = p_text.split()
    return " ".join(word_list)


def focus_item(p_obj):
    p_obj.clear()
    p_obj.setFocus()



def tr_upper(word):
    word = re.sub(r"i", "İ", word)
    word = re.sub(r"ı", "I", word)
    word = re.sub(r"ç", "Ç", word)
    word = re.sub(r"ş", "Ş", word)
    word = re.sub(r"ü", "Ü", word)
    word = re.sub(r"ğ", "Ğ", word)
    word = word.upper()  # for the rest use default upper
    return word


def tr_lower(word):
    word = re.sub(r"İ", "i", word)
    word = re.sub(r"I", "ı", word)
    word = re.sub(r"Ç", "ç", word)
    word = re.sub(r"Ş", "ş", word)
    word = re.sub(r"Ü", "ü", word)
    word = re.sub(r"Ğ", "ğ", word)
    word = word.lower()  # for the rest use default lower
    return word


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
            first_letter = re.sub(r"u", "U", first_letter)
            first_letter = re.sub(r"ü", "Ü", first_letter)
            first_letter = re.sub(r"ğ", "Ğ", first_letter)

            last_part = re.sub(r"İ", "i", last_part)
            last_part = re.sub(r"I", "ı", last_part)
            last_part = re.sub(r"Ç", "ç", last_part)
            last_part = re.sub(r"Ş", "ş", last_part)
            last_part = re.sub(r"U", "u", last_part)
            last_part = re.sub(r"Ü", "ü", last_part)
            last_part = re.sub(r"Ğ", "ğ", last_part)

            rebuilt_word = first_letter + last_part
            rebuilt_word = rebuilt_word.capitalize()
            new_word = new_word + " " + rebuilt_word

        new_word = new_word.strip()
        return new_word
    return ""


