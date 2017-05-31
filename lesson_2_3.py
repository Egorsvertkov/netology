import json
import re
import chardet

list_of_files = ['newsafr.json', 'newscy.json', 'newsfr.json', 'newsit.json']

def get_encodings_chart():
        encodings_chart = {}
        for file in list_of_files:
                with open(file, 'rb') as f:
                    data = f.read()
                    result = chardet.detect(data)
                    encodings_chart[file] = result['encoding']
        return(encodings_chart)

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

def get_top_words_from_newsit():
        with open('newsit.json', encoding=get_encodings_chart()['newsit.json']) as f:
                chart = {}

                data = json.load(f)
                for i in data['rss']['channel']['item']:
                        description_list_raw = i['description'].split()
                        for word in get_clean_description_list(description_list_raw):
                                if len(word) > 6 and word.isalpha():
                                        if word not in chart:
                                                chart[word] = 1
                                        else:
                                                chart[word] += 1
        print('newsit.json')
        print_top_words(get_list_of_counts_from_chart(chart), chart)

def get_top_words_from_newsafr():
    with open('newsafr.json', encoding=get_encodings_chart()['newsafr.json']) as f:
        chart = {}
        data = json.load(f)
        for i in data['rss']['channel']['item']:
            description_list_raw = i['description']['__cdata'].split()
            for word in get_clean_description_list(description_list_raw):
                if len(word) > 6 and word.isalpha():
                    if word not in chart:
                        chart[word] = 1
                    else:
                        chart[word] += 1
    print('newsafr.json')
    print_top_words(get_list_of_counts_from_chart(chart), chart)

def get_top_words_from_newsfr():
    with open('newsfr.json', encoding=get_encodings_chart()['newsfr.json']) as f:
        chart = {}
        data = json.load(f)
        for i in data['rss']['channel']['item']:
            description_list_raw = i['description']['__cdata'].split()
            for word in get_clean_description_list(description_list_raw):
                if len(word) > 6 and word.isalpha():
                    if word not in chart:
                        chart[word] = 1
                    else:
                        chart[word] += 1
    print('newsfr.json')
    print_top_words(get_list_of_counts_from_chart(chart), chart)

def get_top_words_from_newscy():
    with open('newscy.json', encoding=get_encodings_chart()['newscy.json']) as f:
        chart = {}
        data = json.load(f)
        for i in data['rss']['channel']['item']:
            description_list_raw = i['description']['__cdata'].split()
            for word in get_clean_description_list(description_list_raw):
                if len(word) > 6 and word.isalpha():
                    if word not in chart:
                        chart[word] = 1
                    else:
                        chart[word] += 1
    print('newscy.json')
    print_top_words(get_list_of_counts_from_chart(chart), chart)

get_top_words_from_newsit()
get_top_words_from_newsfr()
get_top_words_from_newsafr()
get_top_words_from_newscy()


