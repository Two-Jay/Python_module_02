class CsvReader():
    fp = None
    
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        try:
            self.fp = open(self.filename, 'r')
        except:
            return None
        print("file opened")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.fp:
            self.fp.close()
        print("file closed")

    def getdata(self):
        try:
            ret = []
            data_length = 0
            line_length = 0
            for line in self.fp:
                data_length += 1
                if data_length == 1 and self.header:
                    continue
                if data_length > self.skip_top:
                    l = line.rstrip('\n').split(self.sep)
                    line_length = len(l) if not line_length else line_length
                    if len(l) != line_length:
                        raise Exception("line length mismatch")
                    ret.append(l)
            return ret[:len(ret) - self.skip_bottom]
        except Exception as e:
            print(e)
            return None

    def getheader(self):
        if self.header:
            self.fp.seek(0)
            return self.fp.readline().rstrip('\n').split(self.sep)
        return None

def pretty_liner(func):
    def wrapper(*args, **kwargs):
        print(f"---- instructions {kwargs.get('keyword')} start here ----")
        func(*args, **kwargs)
        print(f"---- instructions {kwargs.get('keyword')} end here ----")
    return wrapper

@pretty_liner
def read_csv(filepath, keyword=None, sep=',', header=False, skip_top=0, skip_bottom=0):
    with CsvReader(filepath, sep, header, skip_top, skip_bottom) as file:
        print(f"file: {filepath}")
        if file:
            print(file.getdata())
        else:
            print("error while opening file")

def main():
    folder_path = "./csv/"
    read_csv(folder_path + "data.csv", keyword="good")
    read_csv(folder_path + "data.csv", keyword="skip_top", skip_top=80)
    read_csv(folder_path + "data.csv", keyword="skip_bottom", skip_bottom=80)
    read_csv(folder_path + "bad.csv", keyword="bad")
    read_csv(folder_path + "bad_length.csv", keyword="bad_length")
    return 0

if __name__ == "__main__":
    main()