import hashlib

with open("salt.txt", "r") as f:
    salt = f.read().strip()
map1 = {}
hashes = []

with open("realhuman_phill.txt", "r", encoding='latin-1') as f:
    for line in f:
        # strip new line character
        password = line.strip()
        # concat salt and password, encode to utf-8
        salted_password = (salt + password).encode('utf-8')
        # hash salted password
        hash_value = hashlib.sha256(salted_password).hexdigest()
        map1[hash_value] = password

# #brite force attack of 4 chracter passwords
# for i in range(0, 26):
#     for j in range(0, 26):
#         for k in range(0, 26):
#             for l in range(0, 26):
#                 password = chr(i + 97) + chr(j + 97) + chr(k + 97) + chr(l + 97)
#                 salted_password = (salt + password).encode('utf-8')
#                 hash_value = hashlib.sha256(salted_password).hexdigest()
#                 map1[hash_value] = password


    # compare hashes to hashes contained in file "hashes.txt"
    with open("hashes.txt", "r", encoding='latin-1') as p:
        linenum = 0
        for line in p:
            linenum += 1
            line = line.strip()
            if map1.get(line) is not None:
                print(linenum, " ", line, ": ", map1[line], " ")
                #output known password to vector
                hashes.append(map1[line])
            else:
                print(linenum, " ", line, ": ")
    #output vector to file
    with open("known_passwords3.txt", "w") as f:
        for i in hashes:
            f.write(i + "\n")