def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words

def sort_on(dict_name):
    return dict_name["num"]

def get_character_count(file_contents):
    lowered_string = file_contents.lower()
    character_count = {}
    for char in lowered_string:
        if not char in character_count:
            character_count[char] = 0
        character_count[char] = character_count[char] + 1
    return character_count

def organise_character_count(character_count):
    organised = []
    for item in character_count:
        organised.append({"char": item, "num": character_count[item]})
    organised.sort(reverse=True, key=sort_on)
    return organised