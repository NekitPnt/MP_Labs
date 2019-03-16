import json
# command for start test in cmd :
# py.test -v pytest_ok.py


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


def test_base():
    posts = read_users_data('original/bloggs.json')
    assert len(posts) != 0, "Empty base!"
    for post in posts:
        assert type(posts[post]) == dict, "Wrong post type in post %s" % post


def test_base2():
    posts = read_users_data('original/bloggs.json')
    assert len(posts) != 0, "Empty base!"
    for post in posts:
        assert type(posts[post]) == dict, "Wrong post type in post %s" % post


def test_taggs():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'taggs' in posts[post], "No taggs block in post %s" % post
        assert type(posts[post]['taggs']) == list, "Wrong taggs type in post %s" % post
        assert len(posts[post]['taggs']) != 0, "Empty taggs on post %s!" % post
        for tag in posts[post]['taggs']:
            assert type(tag) == str, "Wrong tagg type in post %s, tagg: %s" % (post, tag)


def test_taggs2():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'taggs' in posts[post], "No taggs block in post %s" % post
        assert type(posts[post]['taggs']) == list, "Wrong taggs type in post %s" % post
        assert len(posts[post]['taggs']) != 0, "Empty taggs on post %s!" % post
        for tag in posts[post]['taggs']:
            assert type(tag) == str, "Wrong tagg type in post %s, tagg: %s" % (post, tag)


def test_taggs3():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'taggs' in posts[post], "No taggs block in post %s" % post
        assert type(posts[post]['taggs']) == list, "Wrong taggs type in post %s" % post
        assert len(posts[post]['taggs']) != 0, "Empty taggs on post %s!" % post
        for tag in posts[post]['taggs']:
            assert type(tag) == str, "Wrong tagg type in post %s, tagg: %s" % (post, tag)


def test_taggs4():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'taggs' in posts[post], "No taggs block in post %s" % post
        assert type(posts[post]['taggs']) == list, "Wrong taggs type in post %s" % post
        assert len(posts[post]['taggs']) != 0, "Empty taggs on post %s!" % post
        for tag in posts[post]['taggs']:
            assert type(tag) == str, "Wrong tagg type in post %s, tagg: %s" % (post, tag)


def test_body():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'body' in posts[post], "No body block in post %s" % post
        assert type(posts[post]['body']) == str, "Wrong body type %s in post %s" % (type(posts[post]['body']), post)


def test_body2():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'body' in posts[post], "No body block in post %s" % post
        assert type(posts[post]['body']) == str, "Wrong body type %s in post %s" % (type(posts[post]['body']), post)


def test_date():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'datetime' in posts[post], "No datetime block in post %s" % post
        assert type(posts[post]['datetime']) == str, "Wrong date type in post %s" % post


def test_date2():
    posts = read_users_data('original/bloggs.json')
    for post in posts:
        assert 'datetime' in posts[post], "No datetime block in post %s" % post
        assert type(posts[post]['datetime']) == str, "Wrong date type in post %s" % post
