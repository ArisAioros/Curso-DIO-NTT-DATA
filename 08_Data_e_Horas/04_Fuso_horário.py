# instalação de biblioteca fuso horário atraves do terminal VSC: pip install pytz
# Comandos para ambiente virtual digite: python -m venv .env //digite: source .env/bin/activate //digite:pip install pytz
import pytz
from datetime import datetime

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)