

def main():
    input_string = "Hello World! Hello Python Module! 0123456789"
    sum = 0
    for i in input_string:
        sum += ord(i)
    print(sum)


if __name__ == '__main__':
    main()