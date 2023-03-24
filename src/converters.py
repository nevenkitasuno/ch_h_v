from datetime import datetime
from datetime import timedelta
import re
# from typing import Optional

# def str_to_datetime(line: str) -> Optional[datetime]:
#TO DO: don't work somewhy; typehint correctly
# намеренно не стал использовать свой StringParse в этой функции,
# т.к. тут мне интереснее как правильно применить typehint
def str_to_datetime(line):
  """
  Returns a datetime object from a string of format "HH:MM [bla bla bla]"

  >>> str_to_datetime("16:20 остановились на роднике")
  datetime.datetime(1900, 1, 1, 16, 20)
  >>> str_to_datetime("16:20")
  datetime.datetime(1900, 1, 1, 16, 20)
  """
  return (datetime.strptime(re.search(r'\b\d?\d:\d\d\b', line).group(0), '%H:%M'))
  
def datetime_to_str(inp: datetime) -> str:
  """
  Returns a string of format [H]H:MM from a datetime object

  >>> datetime_to_str(datetime(1900, 1, 1, 18, 1))
  '18:01'
  >>> datetime_to_str(datetime(1900, 1, 1, 8, 20))
  '8:20'
  """
  return ("{:d}:{:02d}".format(inp.hour, inp.minute))

def timedelta_to_str(inp: timedelta) -> str:
  """
  Returns a string of format HH:MM from a timedelta object

  >>> timedelta_to_str(timedelta(0, 0, 0, 0, 24, 5, 0))
  '5:24'
  >>> timedelta_to_str(timedelta(0, 0, 0, 0, 21, 18, 0))
  '18:21'
  """
  seconds = inp.total_seconds()
  hours = int(seconds // 3600)
  minutes = int((seconds % 3600) // 60)
  return ("{:d}:{:02d}".format(hours, minutes))