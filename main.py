import re
import argparse

parser = argparse.ArgumentParser(description='Word generator v1.0')
parser.add_argument('word', type=str, help='Word to generate')
parser.add_argument('file_name', type=str, help='Word to generate')
args = parser.parse_args()

def main_functon(word, file_name):
    simbols = [*'!@#$._-']
    simbols_2 = ['!@','!@#','@!']
    numbers = [*'1234567890']
    coombinations_numbers6 = ['!23456','1@3456','12#456','123$56','1234%6','12345^','!@#456','123$%^','123!@#','!@#123']
    years = [str(year) for year in range(2015,2022)]
    mass_words = []
    mass_words_done = []

    file = open(file_name,'a+')

    for index,value in enumerate(word):
        if value.isalpha():
            a = word[:index]
            b = word[index+1:]
            mass_words.append(''.join((a,value.upper(),b)))
    mass_words.append(word)
    for mw in mass_words:
        if re.findall('e',mw):
            done = re.sub('e','3',mw)
            mass_words.append(done)
        if re.findall('a',mw):
            done = re.sub('a','@',mw)
            mass_words.append(done)
        if re.findall('o',mw):
            done = re.sub('o','0',mw)
            mass_words.append(done)
        if re.findall('i',mw):
            done = re.sub('i','!',mw)
            mass_words.append(done)
        if re.findall('s',mw):
            done = re.sub('s','$',mw)
            mass_words.append(done)
    for mw in mass_words:
        for n in numbers:
            for s in simbols:
                mass_words_done.append(mw + n + s)
                mass_words_done.append(mw + s + n)
                mass_words_done.append(n + s + mw)
                mass_words_done.append(s + n + mw)
    for mw in mass_words:
        for c_n in coombinations_numbers6:
            mass_words_done.append(mw + c_n)
            mass_words_done.append(c_n + mw)
    for mw in mass_words:
        for y in years:
            for s in simbols:
                mass_words_done.append(mw + y + s)
                mass_words_done.append(mw + s + y)
    for mw in mass_words:
        for y in years:
            for s in simbols_2:
                mass_words_done.append(mw + y + s)
                mass_words_done.append(mw + s + y)

    for mwd in mass_words_done:
        file.write(mwd+'\n')
    print('Quantity strings: ' + str(len(mass_words_done)))

main_functon(args.word,args.file_name)

