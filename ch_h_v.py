import argparse
import re
import datetime
from datetime import timedelta

def time_from_str(str):
  return (datetime.datetime.strptime(re.search(r'\b\d?\d:\d\d\b', str).group(0), '%H:%M'))
  
def datetime_to_str(inp):
  return ("{:d}:{:02d}".format(inp.hour, inp.minute))

def timedelta_to_str(inp):
  seconds = inp.total_seconds()
  hours = int(seconds // 3600)
  minutes = int((seconds % 3600) // 60)
  return ("{:d}:{:02d}".format(hours, minutes))

parser = argparse.ArgumentParser(
                    prog = 'ch_h_v',
                    description = 'Скрипт для подсчёта чистого ходового времени из текстового файла с отчётом',
                    epilog = 'Файл должен быть нужного формата, см. README.md')

parser.add_argument('-f', '--filename', help="Файл с отчётом")
parser.add_argument('-v', '--verbose', action='store_true', help="Вывод промежуточных значений. Может пригодиться для проверки.")

args = parser.parse_args()

with open(args.filename) as f:
  content = f.read().splitlines()

day_regex = r"День \d{1,2}"
halt_regex = r"\d{1,2}:\d{2} - \d{1,2}:\d{2} (привал|остановились|остановка)"
start_regex = r"\d{1,2}:\d{2} (вышли)"
finish_regex = r"\d{1,2}:\d{2} (встали)"

for line in content:
  if re.match(day_regex, line):
    day_line = line
    if (args.verbose):
      print()
      print(day_line)
  if re.match(start_regex, line):
    time_start = time_from_str(line)
    halt_time = timedelta()
  if re.match(halt_regex, line):
    parts = line.split(' - ')
    time_pause = time_from_str(parts[0])
    time_resume = time_from_str(parts[1])
    halt_time += time_resume - time_pause
    if (args.verbose): print(halt_time)
  if re.match(finish_regex, line):
    time_finish = time_from_str(line)
    total_day_time = time_finish - time_start - halt_time
    if (args.verbose):
      print(day_line + ' ЧХВ = '
            + datetime_to_str(time_finish)
            + ' - ' + datetime_to_str(time_start)
            + ' - ' + timedelta_to_str(halt_time)
            + ' = ' + timedelta_to_str(total_day_time))
    else:
      print(day_line + ' ЧХВ = ' + timedelta_to_str(total_day_time))
