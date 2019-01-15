from Word_List import WordList
import Gui
import json


def create_pic_list(word_list):
    pic_list = []
    for i in word_list:
        pic_list.append('Pics/{}.jpg'.format(i))
    return pic_list


A = WordList("words.txt", "extra_words.txt")

delay = 5000
image_files = create_pic_list(A.all_word_lists[0])

data = json.dumps(image_files)
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

with open('data.json') as json_file:
    data1 = json.load(json_file)
print(data1)
