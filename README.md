# GitTutorial

Gereksinimleri kurma

```bash
pip install -r requirements.txt
```

Rakamdan yazıya çevirme

```bash
python cevir.py
```
# 🛠️ YZ Projesini Nasıl Çalıştıracaksınız?

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

```bash
./start.sh
```

ya da

Dokerize yapmak için ilgisayarınızda Docker ve Docker Compose'un kurulu olduğundan emin olun.

Terminali açıp proje klasörünüze gidin.

Şu komutu çalıştırın:

```bash
docker-compose up --build -d
```

Tarayıcınızdan http://localhost:8000/docs adresine gidin. FastAPI'nin otomatik hazırladığı harika bir arayüz (Swagger UI) sizi karşılayacak.

/predict kısmına tıklayıp, Try it out diyerek şu şekilde bir JSON gönderin:

```plaintext
{
  "text": "I love learning Python!"
}
```

Sistem size anında o metnin pozitif olduğunu söyleyecektir.
