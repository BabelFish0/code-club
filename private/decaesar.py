import caesar as c

if __name__ == '__main__':
    import sys
    message = sys.argv[1]
    assert type(message) == str
    print(f"decoding {message}")
    print(c.decode(message))