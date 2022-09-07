######################################   MODEL OF WORD CORRECTION FUNCTION (RNN biderectionel with LSTM) just saving modele#############################################

def model_correction_fit(pathfile,model_path):
    import tensorflow as tf
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.layers import Embedding, LSTM, Dense, Bidirectional
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.optimizers import Adam
    import numpy as np

    ######################################################################
    tokenizer = Tokenizer()
    data = open(pathfile, encoding="utf8").read()
    corpus = data.split("\n")
    for i in corpus:
        if i == "":
            corpus.remove('')
    corpus = corpus[1:-1]
    corpus_new = []
    for st in corpus:
        ch = " ".join(st)
        corpus_new.append(ch)
    tokenizer.fit_on_texts(corpus_new)
    total_words = len(tokenizer.word_index) + 1
    #############################################################################
    input_sequences = []
    for line in corpus_new:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i + 1]
            input_sequences.append(n_gram_sequence)

    # pad sequences
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

    # create predictors and label
    xs, labels = input_sequences[:, :-1], input_sequences[:, -1]

    ys = tf.keras.utils.to_categorical(labels, num_classes=total_words)
    ####################################################################################
    model = Sequential()
    model.add(Embedding(total_words, 100, input_length=max_sequence_len - 1))
    model.add(Bidirectional(LSTM(100)))
    model.add(Dense(total_words, activation='softmax'))
    adam = Adam(lr=0.001)
    model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['accuracy'])
    model.fit(xs, ys, epochs=100, verbose=1)
    return model.save(model_path, save_format="h5")
######################################## CORRECTION WORD FUNCTION #####################################################
def auto_correction_word(bad_word,model_path,data_path):
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow import keras
    import numpy as np
    model = keras.models.load_model(model_path)
    tokenizer = Tokenizer()
    data = open(data_path, encoding="utf8").read()
    corpus = data.split("\n")
    for i in corpus:
        if i == "":
            corpus.remove('')
    corpus = corpus[1:-1]
    corpus_new = []
    for st in corpus:
        ch = " ".join(st)
        corpus_new.append(ch)
    tokenizer.fit_on_texts(corpus_new)
    total_words = len(tokenizer.word_index) + 1
    #############################################################################
    input_sequences = []
    for line in corpus_new:
        token_list = tokenizer.texts_to_sequences([line])[0]
        for i in range(1, len(token_list)):
            n_gram_sequence = token_list[:i + 1]
            input_sequences.append(n_gram_sequence)

    # pad sequences
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
    counter = len(bad_word)
    for i in range(counter):
        if (ord(bad_word[i]) in [i for i in range(285)]) == True:
            seed_text = " ".join(bad_word[:i])
            noTraited_text = " ".join(bad_word[i + 1:])
            next_words = 100

            for _ in range(next_words):
                token_list = tokenizer.texts_to_sequences([seed_text])[0]
                token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
                #     predicted = model.predict_classes(token_list, verbose=0)
                predicted = np.argmax(model.predict(token_list), axis=1)
                output_word = ""
                for word, index in tokenizer.word_index.items():
                    if index == predicted:
                        output_word = word
                        break
            seed_text += " " + output_word + " " + noTraited_text
            bad_word = "".join(seed_text.split())
    return bad_word
############################################# COMPILATION #############################################################

################simulation#############################################################################################
data1={'الإسم' :'هشا!','اللقب':'السعيد!','المهنة':'معلم'}
data2={'الإسم' :'هش!م','اللقب':'السعي?ي','المهنة':'معلم'}
data3={'الإسم' :'عل!','اللقب':'الماجر!','المهنة':'معلم'}
data4={'الإسم' :'ع?ي','اللقب':'السنو?ي','المهنة':'مع//'}
data5={'الإسم' :'أحم?','اللقب':'م8جوب','المهنة':'معلم'}
data6={'الإسم' :'أح9د','اللقب':'الڨاسم!','المهنة':'معلم'}
data7={'الإسم' :'أح9§','اللقب':'الڨاسم!','المهنة':'معلم'}
data8={'الإسم' :'أ!9§','اللقب':'الڨاسم!','المهنة':'معلم'}
data9={'الإسم' :'!ح9§','اللقب':'الڨاسم!','المهنة':'معلم'}
all_data=[data1,data2,data3,data4,data5,data6,data7,data8,data9]
#1-creation of model:(PS:just train one time but there is all model file)
# model_correction_fit('first_name.csv','model_first_name')
# model_correction_fit('last_name.csv','model_last_name')
# model_correction_fit('job_name.csv','model_job_name')
#2-word correction:
#a-simulation :
for data in all_data:
    for key, value in data.items():
        if key == 'الإسم':
            data_path = 'first_name.csv'
            model_path = 'model_first_name'
            data[key] = auto_correction_word(value, model_path, data_path)
        if key == 'اللقب':
            data_path = 'last_name.csv'
            model_path = 'model_last_name'
            data[key] = auto_correction_word(value, model_path, data_path)
        if key == 'المهنة':
            data_path = 'job_name.csv'
            model_path = 'model_job_name'
            data[key] = auto_correction_word(value, model_path, data_path)

    print(data)
print(all_data)

