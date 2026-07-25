# виправлення одруківки з adwentures на adventures у назві змінних

adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adventures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adventures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adventures_of_tom_sawer = adventures_of_tom_sawer.replace("\n", " ")
# task 02 ==
""" Замініть .... на пробіл
"""
adventures_of_tom_sawer = adventures_of_tom_sawer.replace("....", " ").strip()
# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adventures_of_tom_sawer = " ".join(adventures_of_tom_sawer.split())
print(adventures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
letter_h_count = adventures_of_tom_sawer.lower().count("h")
print(f'У тексті зустрічається літера "h" {letter_h_count} разів.')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words_list = adventures_of_tom_sawer.split()
capital_words_count = 0
for word in words_list:
    first_letter = word.strip('"\'.,;:!?')[0]
    if first_letter.isupper():
        capital_words_count += 1

print(f'У тексті починається з Великої літери {capital_words_count} слів.')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_position = adventures_of_tom_sawer.find("Tom")
second_position = adventures_of_tom_sawer.find("Tom", first_position + 1)

print(f'Слово "Tom" вдруге зустрічається на позиції {second_position}.')

# task 07
""" Розділіть змінну adventures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adventures_of_tom_sawer_sentences
"""
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split('.')
print(f"Результат поділу змінної adventures_of_tom_sawer по кінцю речення - {adventures_of_tom_sawer_sentences}.")

# task 08
""" Виведіть четверте речення з adventures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adventures_of_tom_sawer_sentences[3]
fourth_sentence = fourth_sentence.lower()
print(fourth_sentence)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""

for sentence in adventures_of_tom_sawer_sentences:
    sentence = sentence.strip()
    if sentence.startswith("By the time"):
        # sentence == True
        print(f"Одне з речень починається з 'By the time'")
        break
else:
    print("Жодне речення не починається з 'By the time'")
    
# task 10
""" Виведіть кількість слів останнього речення з adventures_of_tom_sawer_sentences.
"""
last_sentence = adventures_of_tom_sawer_sentences[-1]

if last_sentence.strip() == "":
    last_sentence = adventures_of_tom_sawer_sentences[-2]
words_in_last_sentence = last_sentence.split()
print(f'В останньому реченні {len(words_in_last_sentence)} слів.')