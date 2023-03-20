import argparse
import re
import sys
import enum
from datetime import timedelta
from typing import List
from typing import Optional

import converters as cvt

def get_halt_time(line: str) -> timedelta:
  """
  Returns time of one halt from str with halt description
  (540 / 60 = 42 - 33 = 9)
  >>> get_halt_time("18:33 - 18:42 остановились на ручье, пополнить запасы воды")
  datetime.timedelta(seconds=540)
  """
  parts = line.split(' - ')
  time_pause = cvt.str_to_datetime(parts[0])
  time_resume = cvt.str_to_datetime(parts[1])
  return time_resume - time_pause

@enum.unique
class e_LineType(enum.Enum):
  day_number = 1
  halt = 2
  start = 3
  finish = 4

def get_line_type(line: str) -> Optional[e_LineType]:
  regexes = {
  e_LineType.day_number: r"День \d{1,2}",
  e_LineType.halt: r"\d{1,2}:\d{2} - \d{1,2}:\d{2} (привал|остановились|остановка)",
  e_LineType.start: r"\d{1,2}:\d{2} (вышли)",
  e_LineType.finish: r"\d{1,2}:\d{2} (встали)"}

  for line_type in e_LineType:
    if re.match(regexes[line_type], line):
      return(line_type)
  
  return None

def get_ch_h_v(inp: List[str], verbose: bool):

  for line in inp:
    if get_line_type(line) == e_LineType.day_number:
      # day started
      day_line = line
      if (verbose):
        print()
        print(day_line)
    # halt time count
    if get_line_type(line) == e_LineType.start:
      time_start = cvt.str_to_datetime(line)
      halt_per_day = timedelta()
    if get_line_type(line) == e_LineType.halt:
      halt_per_day += get_halt_time(line)
      if (verbose): print(halt_per_day)
    if get_line_type(line) == e_LineType.finish:
      # day finished
      time_finish = cvt.str_to_datetime(line)
      total_day_time = time_finish - time_start - halt_per_day
      if (verbose):
        print(day_line + ' ЧХВ = '
              + cvt.datetime_to_str(time_finish)
              + ' - ' + cvt.datetime_to_str(time_start)
              + ' - ' + cvt.timedelta_to_str(halt_per_day)
              + ' = ' + cvt.timedelta_to_str(total_day_time))
      else:
        print(day_line + ' ЧХВ = ' + cvt.timedelta_to_str(total_day_time))

def get_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(
                      prog = 'ch_h_v',
                      description = 'Скрипт для подсчёта чистого ходового времени из текстового файла с отчётом',
                      epilog = 'Файл должен быть нужного формата, см. README.md')

  parser.add_argument('-f', '--filename', help="Файл с отчётом")
  parser.add_argument('-v', '--verbose', action='store_true', help="Вывод промежуточных значений. Может пригодиться для проверки.")

  args = parser.parse_args()

  return (args)

def main():
  
  args = get_args()

  if (not args.filename):
    content = sys.stdin.read().splitlines()
  else:
    with open(args.filename) as f:
      content = f.read().splitlines()
  
  get_ch_h_v(content, args.verbose)

if __name__ == '__main__':
  main()