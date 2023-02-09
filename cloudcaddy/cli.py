import argparse
import requests

def make_request(url):
    response = requests.get(url)
    return response.text

# if __name__ == "__main__":
def cli():
    parser = argparse.ArgumentParser(description='Make a HTTP request to the specified URL.')
    parser.add_argument('url', type=str, help='The URL to make a request to.')
    args = parser.parse_args()
    print(make_request(args.url))
