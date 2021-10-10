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
