ru_en = {}

with open("en-ru.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        parts = line.split(" - ")
        if len(parts) != 2:
            continue  # пропускаем строки с ошибками

        en_word = parts[0]
        ru_words = parts[1].split(", ")

        for ru in ru_words:
            if ru not in ru_en:
                ru_en[ru] = [en_word]
            else:
                if en_word not in ru_en[ru]:
                    ru_en[ru].append(en_word)

with open("ru-en.txt", "w", encoding="utf-8") as output:
    for ru_word in sorted(ru_en):
        en_list = sorted(ru_en[ru_word])
        output.write(ru_word + " – " + ", ".join(en_list) + "\n")