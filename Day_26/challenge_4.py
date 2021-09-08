sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

list = sentence.split()
len_words = {word:len(word) for word in list}
print(len_words)


for word in sentence.split():
    print(word)