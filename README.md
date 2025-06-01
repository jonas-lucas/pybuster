# PyBuster

This repository contains a **Python-based** tool for **URL and directory busting**, designed to assist in web reconnaissance, penetration testing, and enumeration tasks.

## How to Use

You must have a reachable **target** and a **wordlist** file.

```bash
python pybuster.py -u http://example.com -w wordlist.txt
```

## How it Works

1. The **target** must be a reachable HTTP or HTTPS server. 

    It can be a **FQDN** or an **IP address** with or without port separeted with `:` *(e.g. 127.0.0.1:8080 or localhost:8080)*.

    If it is a HTTPS server, the default por is 443 else the default port is 80.

2. The **wordlist** must be a file with words for possibles entries to the target.

    The words must be separred with escape line.

    ```python
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]
    ```

3. HTTPConnection

    http.client.HTTPConnection()

## Systems Settings

- Python 3.13.3

## To-Do

- Refact the code
- Add multithreading
- Conclude the README.md

---

### Author

[Jonas Lima](https://github.com/jonas-lucas)