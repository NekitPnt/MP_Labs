#----------------TASK------------------------------------
#Опишите функцию группирующую записи блогов по тегам
#(у записи может быть более одного тега),
#внутри группы записи должны быть отсортированы по дате.

import json

def read_users_data(link):
    try:
        read_file = open(link, "r")
    except:
        with open(link, "w") as read_file:
            json.dump({}, read_file, indent = 4, ensure_ascii = False)
    else:
        with read_file:
            data = json.load(read_file)
        return data
    
def group(link):
    posts = read_users_data(link)
    
    # получение списка тегов
    taggs_list = sorted(list(set([tag for post in posts for tag in posts[post]['taggs']])))
    
    # генерация словаря тегов и соответствующим им списков постов и сортировка постов внутри каждого тега по дате
    def get_post(tag):
         return sorted([(post, posts[post]["datetime"], posts[post]['body']) for post in posts if tag in posts[post]['taggs']], key = lambda kek: kek[1])
    tags_dict = {tag:get_post(tag) for tag in taggs_list}
    
    res = "\n"
    result = ''
    for tag in tags_dict:
        result += '\n-------'+tag.upper()+'-------\n'
        result += res.join(["%s\n%s\n%s\n"% (post[0], post[2], post[1]) for post in tags_dict[tag]])
       
    return result

print(group('bloggs.json'))
