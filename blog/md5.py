import hashlib

def md_5(pwd):
    return hashlib.md5(pwd.encode('utf8')).hexdigest()

if __name__ == '__main__':
    print(md_5('123456'))