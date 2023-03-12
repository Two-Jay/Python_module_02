import faker
import argparse

def csv_generator():
    fake = faker.Faker()
    for i in range(100):
        yield f"{i},{fake.name()},{fake.email()},{fake.phone_number()}\n"

def main(file):
    for i in csv_generator():
        with open(file, 'a') as f:
            f.write(i)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default='data.csv', help='file to write to')
    return parser.parse_args()

if __name__ == '__main__':
    main(parse_args().file)