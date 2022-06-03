# YENİ REPOSITORY OLUŞTURMAK:

echo "# GitTutorial" >> README.md

git add README.md

git commit -m "first commit"

git remote add origin https://github.com/42htuna/GitTutorial.git

git push -u origin master



## YENİ BRANCH OLUŞTURMAK:

git checkout -b newBranch

git commit -m “Yeni Branch Eklendi”

git push origin newBranch



# KOMUT SATIRINDAN ÇALIŞAN PYTHON KODLARI:

```
python -c "import string; from random import * ; c=string.digits + string.ascii_letters + string.punctuation; a=''.join(choice(c) for x in range(randint(8, 13))); print(a)"

python -c "import string; from random import * ; print(''.join(choice(string.digits) for i in range(randint(8, 13))))"

python -c "a=['192.168.{}.{}'.format(i, j) for i in range(256) for j in range(256)]; print(a)"

python -c "from random import *; x=['551-{}-{}-{}'.format(a,b,c) for a in range(999+1) for b in range(99+1) for c in range(99+1)]; print(x)"

python -c "import string; from random import * ; print(''.join(choice(string.digits) for i in range(randint(7, 7))))"

python -c "import string; from random import * ; x=''.join(choice(string.digits) for i in range(randint(7, 7))); c='551-{}'.format(x); print(c)"

python -c "import string; from random import * ; i=''.join(choice(string.digits) for i in range(randint(3, 3))); j=''.join(choice(string.digits) for i in range(randint(2,2))); g=''.join(choice(string.digits) for i in range(randint(2,2))); c='+90 551 {} {} {}'.format(i,j,g); print(c)"
```


## DJANGO VERSION:

```
python -c "import django; print(django.VERSION)"
```


## KABUK GEÇMİŞİNİ TEMİZLEME:

```
import readline

readline.clear_history()
```

