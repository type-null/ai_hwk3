"""
Pre-processing glove file,
translate into indexed dictionary.
"""


glove_file = 'glove.twitter.27B.25d.txt'
glove = open(f"../../../../../Downloads/glove/{glove_file}")
index_dict = open("index_dict.txt", "w")
for line in glove:
    values = line.split()
    word = values[0]
    # vector = np.asarray(values[1:], dtype='float32')
    # emb_dict[word] = vector
    index_dict.write(f"{word}\n")
glove.close()
index_dict.close()