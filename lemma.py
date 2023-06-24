from konlpy.tag import Okt
from konlpy.tag import Kkma
import glob

okt = Okt()
kkma = Kkma()

for filename in glob.glob('/Users/choiboyoung/소융캡/넷플릭스_리뷰_크롤링/*.csv'):
    title = filename[35:-4]
    stop_words_list = []
    for word, pos in okt.pos(title, norm=True, stem=True):
        if pos in ('Noun', 'Adjective', 'Verb', 'Adverb'):
            stop_words_list.append(word)
    
    try:
        with open(filename[:-4] + '_character.txt', 'r', encoding='utf-8-sig') as g:
            texts = g.readlines()
            for line in texts:
                stop_words_list.append(line.strip())
            print(stop_words_list)
        
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            lemmatized_words = []
        for word, pos in okt.pos(text, norm=True, stem=True):
            if pos in ('Noun', 'Adjective', 'Verb', 'Adverb'):
                if word not in (stop_words_list):
                    if len(word) > 1:
                        if '하다' in word:
                            lemmatized_words.append(word[:-2])
                        else:
                            lemmatized_words.append(word)
            else:
                pass
        with open(filename[:-4] + '_lemma', 'w', encoding='utf-8') as g:
            for word in lemmatized_words:
                g.write(str(word))
                g.write('\n')
            g.close()
    except:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
            lemmatized_words = []
        for word, pos in okt.pos(text, norm=True, stem=True):
            if pos in ('Noun', 'Adjective', 'Verb', 'Adverb'):
                if pos not in (stop_words_list):
                    if len(word) > 1:
                        if '하다' in word:
                            lemmatized_words.append(word[:-2])
                        else:
                            lemmatized_words.append(word)
            else:
                pass
        with open(filename[:-4] + '_lemma', 'w', encoding='utf-8') as g:
            for word in lemmatized_words:
                g.write(str(word))
                g.write('\n')
            g.close()