import json
import re
import chardet

list_of_files = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

def get_clean_description_list(raw_list):
        description_list = []
        for word in raw_list:
            result = re.sub('[\,\.\(]*(\w+)[\,\.\)]', r'\1', word)
            description_list.append(result)
        return(description_list)

def get_list_of_counts_from_chart(random_chart):
        list_of_counts = []
        for k, v in random_chart.items():
            if v not in list_of_counts:
                list_of_counts.append(v)
        list_of_counts.sort(reverse=True)
        return list_of_counts

def print_top_words(random_list_of_counts, random_chart):
        counter = 0
        for i in random_list_of_counts:
            for k, v in random_chart.items():
                if v == i:
                    counter += 1
                    if counter <= 10:
                        print(k, v)
                    else:
                        break

def get_top_words_from_file(filename):
        with open(filename, 'rb') as f:
                chart = {}
                text = f.read()
                json_text = text.decode(chardet.detect(text)['encoding'])
                data = json.loads(json_text)
                for i in data['rss']['channel']['item']:
                        if filename == 'newsit.json':
                                description_list_raw = i['description'].split()
                        else:
                                description_list_raw = i['description']['__cdata'].split()
                        for word in get_clean_description_list(description_list_raw):
                                if len(word) > 6 and word.isalpha():
                                        if word not in chart:
                                                chart[word] = 1
                                        else:
                                                chart[word] += 1
        print(filename)
        print_top_words(get_list_of_counts_from_chart(chart), chart)

for file in list_of_files:
        get_top_words_from_file(file)




