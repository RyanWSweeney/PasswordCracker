import hashlib
from itertools import islice

with open("salt.txt", "r") as f:
    salt = f.read().strip()
map1 = {}
hashes = []

# with open("realhuman_phill.txt", "r", encoding='latin-1') as f:
#     for line in f:
#         # strip new line character
#         password = line.strip()
#         # concat salt and password, encode to utf-8
#         salted_password = (salt + password).encode('utf-8')
#         # hash salted password
#         hash_value = hashlib.sha256(salted_password).hexdigest()
#         map1[hash_value] = password

with open("known_passwords3.txt", "r", encoding='latin-1') as infile:
    running = True
    millions = 0
    # while not at end of file
    while running:
        millions += 1
        print(millions)
        lines_gen = list(islice(infile, 10000000))
        if not lines_gen:
            running = False
            break
        for line in lines_gen:
            # if line is end of file, set running to false
            # strip new line character
            password = line.strip()
            # concat salt and password, encode to utf-8
            salted_password = (salt + password).encode('utf-8')
            # hash salted password
            hash_value = hashlib.sha256(salted_password).hexdigest()
            map1[hash_value] = password
        # compare hashes to hashes contained in file "hashes.txt"
        with open("hashes.txt", "r", encoding='latin-1') as p:
            linenum = 0
            for line in p:
                linenum += 1
                line = line.strip()
                if map1.get(line) is not None:
                    # output known password to vector
                    #only output if not already in vector
                    if map1[line] not in hashes:
                        hashes.append(map1[line])
        # empty map
        map1.clear()

    # print hashes stored in hashes
    print(hashes)
    # print number of hashes
    print(len(hashes))

    map2 = {}
    # hash the words found in hashes
    for i in hashes:
        salted_password = (salt + i).encode('utf-8')
        hash_value = hashlib.sha256(salted_password).hexdigest()
        map2[hash_value] = i

    # compare hashes to hashes contained in file "hashes.txt"
    with open("hashes.txt", "r", encoding='latin-1') as p:
        linenum = 0
        for line in p:
            line = line.strip()
            if map2.get(line) is not None:
                print(linenum, " ", line, " ", map2[line])
            else:
                print(linenum, " ", line, " ")
            linenum += 1

    # output vector to file
    with open("known_passwords4.txt", "w") as f:
        for i in hashes:
            f.write(i + "\n")
