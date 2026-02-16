from datetime import datetime
import time

epoch = datetime(1970, 1, 1)
print(f"Seconds since {epoch.strftime('%B')} {epoch.day}, {epoch.year} : \
{time.time():,.4f} or {time.time():.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))