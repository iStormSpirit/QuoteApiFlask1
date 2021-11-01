## О проекте 
Суть проекта QuoteApiFlask1 - познакомиться с фрейморком flask, написав простой api с возможностью создавать автора, цитаты у автора и присваивать им рейтинг с используюя метод 

##Run project
```
python3 -m venv flask_venv
source flask_venv/bin/activate
pip install -r requirements.txt
flask db upgrade
python app.py
```
### Без бд
```
flask db init
flask db migrate -m "Initial"
flask db upgrade
```
