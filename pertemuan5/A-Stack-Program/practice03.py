def balik_string(alphabet):
    pembalik = []

    for teks in alphabet:
        pembalik.append(teks)
    hasil = ''

    if pembalik != []:
        while pembalik  :
            hasil += pembalik.pop()
        return hasil

print(balik_string(""))
# print(balik_string("Yang ytta aja"))