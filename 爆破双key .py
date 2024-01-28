flag = [102,108,97,103,123]
for key in range(1,100):
    for keykey in range(1,100):
        ciphertext = []
        for f in flag:
            ciphertext.append((key * f + keykey) % 256)
            if bytes(ciphertext).hex()[:10] == 'dd4388ee42':
                print(key)
                print(keykey)
print('asd')

#17 23

cipher = ['dd','43','88','ee','42','8b','dd','dd','58','65','cc','66','aa','58','87','ff','cc','a9','66','10','9c','66','ed','cc','a9','20','66','7a','88','31','20','64']
a = 0
res = []
for j in range(0,32):
    for i in range(10,150):
        ciphertext = []
        ciphertext.append((i*17+23)%256)
        if bytes(ciphertext).hex() == cipher[j]:
            res.append(i)
            print(i)
            break
print(bytes(res))
