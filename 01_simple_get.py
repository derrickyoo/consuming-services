import requests

def main():
    url = 'https://github.com'
    resp = requests.get(url)
    print(resp.status, resp.text[:50])

if __name__ == '__main__':
    main()
