# find() ve index()
# Aranan karakterin veya kelimenin yerini bulurlar. Ama bunu sayı ile verir.
# Yani metin değişkeni içerisinde bir kelime ya da karakter arıyorsak
# find() ve index() metodları bize onun kaçıncı karakterde başladığını söyler.
# karakterleri saymaya 0'dan başlarlar. 0,1,2,3... gibi:
metin = """Buraya ayazdığım metin değişkeni içerisine ilk önce ingilizce yazmak
istedim ama aklıma bi şey gelmedi. Sonra bu yazdığımı ingilizce yazabilirim di-
ye düşündüm:
I had want to write here in English what I will write in variable."""
print(metin.find("I"))
162
print(metin.find("had"))
164
print(metin.index("I"))
162
print(metin.count("had"))
164
# Her ikisi de ilk bulduğunu verir. Yani "I" karakterini veya "had" kelimesini
# ilk nerede gördüyse o sırayı yazar.

# index ayrıca tersten de yazdırır:
sayılar = ("1","2","3","3","5","6","2","4","8","12","156","123","456","568")
print(sayılar[-1])
568 # -1 yazdığım için sondan yazdırdı.
print(sayılar[1:-1])
('2', '3', '3', '5', '6', '2', '4', '8', '12', '156', '123', '456')
