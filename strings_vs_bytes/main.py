def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "text as string"
    print(s)

    # s+b gives error, we cannot combine strings and bytes
    # we have to decode  bytes to UTF-8 or any appropriate encoding
    # then we can combine.
    string2 = b.decode('utf-8')

    print(s + string2)

    # Now we can append bytes by encoding string to bytes.
    bytes_2 = s.encode()

    print(b + bytes_2)

    # Encoding String to UTF-32, to get bytes.
    print(s.encode('UTF-32'))


if __name__ == "__main__":
    main()
