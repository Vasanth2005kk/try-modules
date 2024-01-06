import secrets
print(dir(secrets))
print(len(dir(secrets)))
print(secrets.__all__)
print(len(secrets.__all__))

#choice
a=(1,2,3,4,5,6,7)
print("choice:",secrets.choice(a))#rendom choice number

#randbelow
print("rendbelow:",secrets.randbelow(10))#only 0 to 10 numbers print it

#SystemRandom
print("randbits:",secrets.randbits(10))#this limit is int(4300) 

#token_bytes
print("token_bytes:",secrets.token_bytes(1))
print("token_bytes_emt:",secrets.token_bytes())

#token_hex
print("token_hex:",secrets.token_hex())
print("token_hex:",secrets.token_hex())

#token_urlsafe
print("token_urlsafe:",secrets.token_urlsafe())
print("token_urlsafe:",secrets.token_urlsafe(10))

#compare_digest
a=8
print(secrets.compare_digest)