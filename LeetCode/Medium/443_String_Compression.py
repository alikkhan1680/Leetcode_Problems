def compress(chars):
    write_index = 0  # Qayerga yozayotganimizni kuzatamiz
    count = 1  # Hozirgi harf nechta takrorlanayotganini hisoblaymiz

    for i in range(1, len(chars) + 1):
        # Agar oxirgi elementgacha kelgan bo'lsak yoki harf o'zgargan bo'lsa
        if i == len(chars) or chars[i] != chars[i - 1]:
            # Harfni yozamiz
            chars[write_index] = chars[i - 1]
            write_index += 1

            # Agar takrorlanish 1 dan katta bo'lsa, uni raqam ko'rinishida yozamiz
            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1

            count = 1  # Hisobni qayta boshlaymiz
        else:
            count += 1  # Takrorlanishni oshiramiz

    return write_index  # Yangi uzunlikni qaytaramiz


chars = ['a', 'a', 'b', 'b', 'b', 'c']
new_length = compress(chars)
print(chars[:new_length])  # ['a', '2', 'b', '3', 'c']
