import json


def read_users_data(link):
    try:
        read_file = open(link, "r")
    except:
        with open(link, "w") as read_file:
            json.dump({}, read_file, indent=4, ensure_ascii=False)
    else:
        with read_file:
            data = json.load(read_file)
        return data


def test_base(link):
    posts = read_users_data(link)
    assert len(posts) != 0, "Empty base!"
    for post in posts:
        assert type(posts[post]) == dict, "Wrong post type in post %s" % post


def test_taggs(link):
    posts = read_users_data(link)
    for post in posts:
        assert 'taggs' in posts[post], "No taggs block in post %s" % post
        assert type(posts[post]['taggs']) == list, "Wrong taggs type in post %s" % post
        assert len(posts[post]['taggs']) != 0, "Empty taggs on post %s!" % post
        for tag in posts[post]['taggs']:
            assert type(tag) == str, "Wrong tagg type in post %s, tagg: %s" % (post, tag)


def test_body(link):
    posts = read_users_data(link)
    for post in posts:
        assert 'body' in posts[post], "No body block in post %s" % post
        assert type(posts[post]['body']) == str, "Wrong body type %s in post %s" % (type(posts[post]['body']), post)


def test_date(link):
    posts = read_users_data(link)
    for post in posts:
        assert 'datetime' in posts[post], "No datetime block in post %s" % post
        assert type(posts[post]['datetime']) == str, "Wrong date type in post %s" % post


if __name__ == "__main__":
    test_base('test1.json')
    test_base('test10.json')
    test_taggs('test2.json')
    test_taggs('test7.json')
    test_taggs('test3.json')
    test_taggs('test9.json')
    test_body('test4.json')
    test_body('test8.json')
    test_date('test5.json')
    test_date('test6.json')
    print("Everything passed")
