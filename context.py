import nltk
import re

def process_tokens(temp_tokens):

    tokens = []
    for token in temp_tokens:
        flag = False
        l = ("-", "\u2212", "\u2014", "\u2013", "/", "~", '"', "'", "\u201C", "\u2019", "\u201D", "\u2018", "\u00B0")
        # \u2013 is en-dash. Used for number to nubmer
        # l = ("-", "\u2212", "\u2014", "\u2013")
        # l = ("\u2013",)
        tokens.extend(re.split("([{}])".format("".join(l)), token))

    return tokens


def word_tokenize(tokens):
    return [token.replace("''", '"').replace("``", '"') for token in nltk.word_tokenize(tokens)]

sent_tokenize = nltk.sent_tokenize
f_w = open('/Users/colin/Downloads/combined_context_Question_processed.txt', 'w')

count = 0
with open('/Users/colin/Downloads/combined_context_Question') as f:
    for line in f:
        if count % 1000 == 0:
            print(count)
        count = count + 1
        context = line
        context = context.replace("''", '" ')
        context = context.replace("``", '" ')
        xi = list(map(word_tokenize, sent_tokenize(context)))
        tags = []
        for xt in xi:
            tokens_tmp = [x if x != '' else ' ' for x in xt]
            ttags = nltk.pos_tag(tokens_tmp)
            tags.append([(x[0] + '_' + x[1]).strip() for x in ttags])

        for x in tags:
            for y in x:
                f_w.write(y+' ')
            f_w.write('\n')


f_w.close()