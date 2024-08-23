import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('Password not on the list.')
        return
    
def main():
    zfile = zipfile.ZipFile('test.zip')
    passfile = open('passlist.txt')
    for line in passfile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print('Password Found = ' + password)
            break
        



if __name__ == '__main__':
    main()        
        