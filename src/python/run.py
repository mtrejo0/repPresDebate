import json
import string

def parse_transcript(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    dialogues = {}
    for line in lines:
        if ': ' in line:
            person, dialogue = line.split(': ', 1)
            if person in dialogues:
                dialogues[person].append(dialogue.strip())
            else:
                added = False
                for name in dialogues:
                    if person.lower() in name.lower():
                        dialogues[name].append(dialogue.strip())
                        added = True
                if not added:
                    dialogues[person] = [dialogue.strip()]

    return dialogues

parsed = parse_transcript("transcript.txt")


for name in ["BRET BAIER, FOX ANCHOR", "MARTHA MACCALLUM, FOX ANCHOR", "JOE BIDEN, PRESIDENT OF THE UNITED STATES",  "UNKNOWN",  "UNIDENTIFIED MALE", "ALEXANDER DIAZ, CATHOLIC UNIVERSITY OF AMERICA"]:
    del parsed[name]


def count_word_frequency(dialogues):
    word_frequency = {}
    word_count = {}

    stop_words = set([
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 
        'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 
        'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
        'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 
        'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
        'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 
        'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
        'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 
        'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
        'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', 
        "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 
        'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 
        'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 
        'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "", "im"
    ])

    for person, lines in dialogues.items():
        # Only consider the part of the name before the first comma
        person = person.split(',')[0]

        if person not in word_frequency:
            word_frequency[person] = {}
            word_count[person] = 0

        for line in lines:
            words = line.split()
            word_count[person] += len(words)
            for word in words:
                word = word.lower().translate(str.maketrans('', '', string.punctuation))
                if word not in stop_words:
                    if word in word_frequency[person]:
                        word_frequency[person][word] += 1
                    else:
                        word_frequency[person][word] = 1

        # Filter out words with frequency less than 2 and sort by frequency
        word_frequency[person] = {k: v for k, v in sorted(word_frequency[person].items(), key=lambda item: item[1], reverse=True) if v > 1}

    return word_frequency, word_count

word_frequency, word_count = count_word_frequency(parsed)

word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))


for person, frequencies in word_frequency.items():
    print(f"{person} (total words: {word_count[person]}): {json.dumps(frequencies, indent=4)}")

# Save word frequency data to a JSON file
with open('word_frequency.json', 'w') as f:
    json.dump(word_frequency, f, indent=4)

# Save word count data to a JSON file
with open('word_count.json', 'w') as f:
    json.dump(word_count, f, indent=4)