import faker

def csv_generator():
    fake = faker.Faker()
    for i in range(100):
        yield fake.name() + ',' + fake.email() + ',' + fake.phone_number() + '\n'

def main():
    for i in csv_generator():
        with open('data.csv', 'a') as f:
            f.write(i)

if __name__ == '__main__':
    main()