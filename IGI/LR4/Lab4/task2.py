import re
import zipfile
import collections

# Задание 2
def task2():
    with open('source.txt', 'r') as file:
        text = file.read()

    results = analyze_text(text)
    save_results_to_file(results, 'results.txt')
    archive_file('results.txt')
    print("Task 2 is done! Check results.txt!")
def analyze_text(text):
    # Количество предложений
    sentences = re.split(r'[.!?]+', text)
    num_sentences = len(sentences)

    # Количество предложений каждого вида
    declarative_sentences = len(re.findall(r'\b[A-Z][^.!?]*', text))
    interrogative_sentences = len(re.findall(r'\b(What|When|Where|Who|Why|How)[^.!?]*', text))
    imperative_sentences = len(re.findall(r'\b(Please|Let)[^.!?]*', text))

    # Средняя длина предложения в символах
    avg_sentence_length = sum(len(sentence.split()) for sentence in sentences) / num_sentences

    # Средняя длина слова в символах
    words = re.findall(r'\b\w+\b', text)
    avg_word_length = sum(len(word) for word in words) / len(words)

    # Количество смайликов
    smiles = re.findall(r'[;:]-*[\(\)\[\]]{2,}', text)
    num_smiles = len(smiles)

    # Email и имена адресатов
    emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    email_names = [email.split('@')[0] for email in emails]

    # Замена $v_(i)$ на v[i]
    text = re.sub(r'\$v_\(([a-zA-Z0-9]+)\)', r'v[\1]', text)

    # Количество слов, начинающихся или заканчивающихся на гласную букву
    vowel_words = re.findall(r'\b[aeiouAEIOU]\w*[aeiouAEIOU]\b', text)
    num_vowel_words = len(vowel_words)

    # Повторяется каждый символ
    char_count = collections.Counter(text)

    # Слова, идущие после запятой
    words_after_comma = re.findall(r',\s(\w+)', text)
    words_after_comma.sort()

    return {
        "num_sentences": num_sentences,
        "declarative_sentences": declarative_sentences,
        "interrogative_sentences": interrogative_sentences,
        "imperative_sentences": imperative_sentences,
        "avg_sentence_length": avg_sentence_length,
        "avg_word_length": avg_word_length,
        "num_smiles": num_smiles,
        "emails": emails,
        "email_names": email_names,
        "text": text,
        "num_vowel_words": num_vowel_words,
        "char_count": char_count,
        "words_after_comma": words_after_comma
    }

def save_results_to_file(results, filename):
    with open(filename, 'w') as file:
        for key, value in results.items():
            file.write(f"{key}: {value}\n")

def archive_file(filename):
    with zipfile.ZipFile(f"{filename}.zip", 'w') as zipf:
        zipf.write(filename)
