import json
import unittest


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


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_base(self):
        posts = read_users_data('test1.json')
        self.assertNotEqual(len(posts), 0)
        for post in posts:
            self.assertEqual(type(posts[post]), dict)

    def test_base2(self):
        posts = read_users_data('test10.json')
        self.assertNotEqual(len(posts), 0)
        for post in posts:
            self.assertEqual(type(posts[post]), dict)

    def test_taggs(self):
        posts = read_users_data('test2.json')
        for post in posts:
            self.assertIn('taggs', posts[post])
            self.assertEqual(type(posts[post]['taggs']), list)
            self.assertNotEqual(len(posts[post]['taggs']), 0)
            for tag in posts[post]['taggs']:
                self.assertEqual(type(tag), str)

    def test_taggs2(self):
        posts = read_users_data('test7.json')
        for post in posts:
            self.assertIn('taggs', posts[post])
            self.assertEqual(type(posts[post]['taggs']), list)
            self.assertNotEqual(len(posts[post]['taggs']), 0)
            for tag in posts[post]['taggs']:
                self.assertEqual(type(tag), str)

    def test_taggs3(self):
        posts = read_users_data('test3.json')
        for post in posts:
            self.assertIn('taggs', posts[post])
            self.assertEqual(type(posts[post]['taggs']), list)
            self.assertNotEqual(len(posts[post]['taggs']), 0)
            for tag in posts[post]['taggs']:
                self.assertEqual(type(tag), str)

    def test_taggs4(self):
        posts = read_users_data('test9.json')
        for post in posts:
            self.assertIn('taggs', posts[post])
            self.assertEqual(type(posts[post]['taggs']), list)
            self.assertNotEqual(len(posts[post]['taggs']), 0)
            for tag in posts[post]['taggs']:
                self.assertEqual(type(tag), str)

    def test_body(self):
        posts = read_users_data('test4.json')
        for post in posts:
            self.assertIn('body', posts[post])
            self.assertEqual(type(posts[post]['body']), str)

    def test_body2(self):
        posts = read_users_data('test8.json')
        for post in posts:
            self.assertIn('body', posts[post])
            self.assertEqual(type(posts[post]['body']), str)

    def test_date(self):
        posts = read_users_data('test5.json')
        for post in posts:
            self.assertIn('datetime', posts[post])
            self.assertEqual(type(posts[post]['datetime']), str)

    def test_date2(self):
        posts = read_users_data('test6.json')
        for post in posts:
            self.assertIn('datetime', posts[post])
            self.assertEqual(type(posts[post]['datetime']), str)


if __name__ == '__main__':
    unittest.main()
