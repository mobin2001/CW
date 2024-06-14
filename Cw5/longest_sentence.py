

with open('test.txt','r') as fin:
    data = fin.read()
    
    data_sentences = data.split('.')

    data_sentences_dict = dict()
    exception_words = ['in','a','to']
    len_sentence = 0
    for sentence in data_sentences:

        count = 0

        
        for word in sentence.split():

            if word not in exception_words:
                count += 1
                

        data_sentences_dict[sentence] = count

sentence_coount = list(data_sentences_dict.items())

sorted_sentence = sorted(sentence_coount,key = lambda x: x[1],reverse= True)

for word in sorted_sentence[0][0]:
    if word not in exception_words:
        len_sentence += len(word)


print(f"The longest sentence is: {sorted_sentence[0][0]}\nLength = {len_sentence}\nWords = {sorted_sentence[0][1]}")





   