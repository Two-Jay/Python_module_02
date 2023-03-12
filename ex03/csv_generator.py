import faker
import argparse

def csv_generator():
    fake = faker.Faker()
    flag = False
    if parse_args().header == True and flag == False:
        yield f"id,name,email,phone_number\n"
        flag = True
    for i in range(100):
        yield f"{i},{fake.name()},{fake.email()},{fake.phone_number()}\n"

def main(args):
    for i in csv_generator():
        with open(args.file, 'a') as f:
            f.write(i)

def parse_args():
    parser = argparse.ArgumentParser()
    folder_path = "./csv/"
    parser.add_argument('-f', '--file', type=str, default= folder_path + 'data.csv', help='file to write to', required=True)
    parser.add_argument('-hd', '--header', type=bool, default=False, help='file to write to')
    return parser.parse_args()

if __name__ == '__main__':
    main(parse_args())