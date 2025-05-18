import os
import argparse
import http.client
from urllib.parse import urlparse


__title__ = 'PyBuster'
__version__ = '0.1'
__author__ = 'Jonas Lima'
__license__ = 'MIT'


def read_wordlist(file_path: str) -> list:
    """Read lines from a wordlist file and return as a list of words."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'The wordlist file "{file_path}" does not exist.')

    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def bust_urls(base_url: str, wordlist: list) -> None:
    """Attempt to access each path in the wordlist and print accessible URLs."""
    parsed_url = urlparse(base_url)

    conn = None
    if parsed_url.scheme == 'https':
        conn = http.client.HTTPSConnection(parsed_url.netloc)
    else:
        conn = http.client.HTTPConnection(parsed_url.netloc)

    for word in wordlist:
        path = f"{parsed_url.path.rstrip('/')}/{word}".replace('//', '/')
        try:
            conn.request("GET", path)
            response = conn.getresponse()

            if response.status < 400:
                print(f" {base_url.rstrip('/')}/{word} (Status: {response.status})")
            response.read()  # Consume response to avoid connection errors
        except Exception as e:
            continue

    conn.close()


def main():
    parser = argparse.ArgumentParser(description='Python-based URL buster.')
    parser.add_argument('-u', '--url', required=True, help='Base URL to scan (e.g., http://example.com/)')
    parser.add_argument('-w', '--wordlist', required=True, help='Path to the wordlist file')
    args = parser.parse_args()

    wordlist = read_wordlist(args.wordlist)

    # Improving the output
    print('='*64)
    print(f' {__title__+' v'+__version__: <31}{__author__: >31} ')
    print('='*64)
    bust_urls(args.url, wordlist)
    print('='*64)


if __name__ == '__main__':
    main()
