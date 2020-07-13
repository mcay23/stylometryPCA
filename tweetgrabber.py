from twitterscraper import query_tweets_from_user
from string import punctuation
from nltk import word_tokenize

def main():
    # with open("x.txt") as f:
    #     for line in f:
    #         line = line.strip()
    #         write_tweets(line, "repub_" + line + ".txt")
    write_tweets('DineshDSouza', 'repub_dineshdsouza.txt')
    write_tweets('GOPLeader', 'repub_gopleader.txt')

    # print('test')
    # line = "\u2341 hey test \u2342 x"
    # line = " ".join(filter(lambda x:('pictwitter' not in x), line.split()))
    # print(line)

def write_tweets(username, filename):
    file = open(filename, "w")
    count = 0
    punct = punctuation + "”“"
    for tweet in query_tweets_from_user(username, 1000):
        line = str(tweet.text.encode('utf-8'))
        # remove punctuation, etc
        line = ' '.join(word for word in line.split(' ') if (not word.startswith('\\') and not word.startswith('pictwitter')))
        line = line.translate(str.maketrans('', '', punct)).lower()
        if line.strip() != '':
            file.write(line[1:].strip() + "\n")
        count = count + 1
    print(str(count) + " actual tweets")
    file.close()

main()
