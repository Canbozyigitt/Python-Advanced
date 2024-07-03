                                         # DateTime Modülü
# timedelta Sınıfı:
# İki tarih arasındaki farkı temsil eder
# Tarih ve saat arasındaki aritmetik işlemleri yapmak için kullanılır.
from datetime import timedelta

today = datetime.now()
tomorrow = today + timedelta(days=1)

print(today)     # Şu anki tarih ve saat
print(tomorrow)  # Yarının tarihi






# timezone ve tzinfo sınıflarıyla zaman dilimleri ve zaman dilimi bilgisi desteği sağlanır
from datetime import datetime, timezone, timedelta

now_utc = datetime.now(timezone.utc)
print(now_utc)  # UTC zaman diliminde şu anki tarih ve saat

eastern_timezone = timezone(timedelta(hours=-5))
eastern_time = now_utc.astimezone(eastern_timezone)
print(eastern_time)  # Doğu Amerika Zaman Diliminde şu anki tarih ve saat
