import caesar as c

if __name__ == '__main__':
    import sys
    message = sys.argv[1]
    assert type(message) == str
    print(f"decoding {message}")
    decoded = c.decode(message)
    print(" "*9 + decoded[0] + " shifted " + str(26 - decoded[1]))