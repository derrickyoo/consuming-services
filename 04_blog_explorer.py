import datetime
import requests
import collections

Post = collections.namedtuple("Post", 'id title content published view_count')

base_url = 'http://consumer_services_api.talkpython.fm/'


def main():
    get_posts()


def get_posts(posts):
    url = base_url + 'api/blog'
    headers = {'Accept': 'application/json'}

    resp = requests.get(url, headers=headers)

    if resp.status_code != 200:
        print('Error downloaindg posts: '.format(resp.status_code, resp.text))

    return [
        Post(**post)
        for post in resp.json()
    ]


def add_post():
    now = datetime.datetime.now()
    published_text = '{}-{}-{}'.format(now.year,
                                       str(now.month).zfill(2),
                                       str(now.day).zfill(2))

    title = input('title: ')
    content = input('content: ')
    view_count = int(input('view count: '))

    post_data = dict(title=title, content=content, view_count=view_count,
                     published_text=published_text)
    url = base_url = base_url + 'api/blog'

    headers = {'content-type': 'application/json'}
    resp = requests.post(url, json=post_data, headers=headers)

    if resp.status != 201:
        print('Error creating post: {} {}'.format(resp.status_code, resp.text))
        return

    post = resp.json()
    print('Created this: ')
    print(post)


if __name__ == '__main__':
    main()
