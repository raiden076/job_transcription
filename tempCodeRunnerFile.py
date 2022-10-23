from datetime import datetime
from zoneinfo import ZoneInfo
print(datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y-%m-%d-%H-%M-%S"))