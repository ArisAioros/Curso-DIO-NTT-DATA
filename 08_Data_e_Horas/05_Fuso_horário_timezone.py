# Criando data e hora com timzone:

from datetime import datetime, timedelta, timezone

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_são_paulo = datetime.now(timezone(timedelta(hours=3)))

print(data_oslo)
print(data_são_paulo)
