import re
fr = open("kool.txt", encoding="utf-8")
fa = open("500 000+ sona.txt", "a", encoding="utf-8")
fr2 = open("500 000+ sona.txt", "r")
count = 0

for line in fr:
    count += 1
    lines_of_words = (re.findall(r"(?i)\b[a-z, öüä]+\b", line))
    words = ', '.join(lines_of_words)
    fa.write(words.split(",", 1)[0])
    print(words.split(",", 1)[0])
print("Sõnasi umbes: " + str(count))

fr2.close()
fr.close()
fa.close()

"""
See on programm on mis convertib webilehelt saadud andmed fili(Saksakeele sonad_500 000+ sona.txt)!
Ja loeb mitu sõna on olemas.
"""
