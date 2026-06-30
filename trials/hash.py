from passlib.hash import django_pbkdf2_sha256

parola=input("Parolayı giriniz: ")

hash=django_pbkdf2_sha256.hash(parola)

print("Parolanızın etiketi : "+hash)

print(django_pbkdf2_sha256.verify(parola, hash))
