import re
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
  """
  Describes line categories, as
  line with a day number, or
  line describing a halt, or
  line declining start/finish of today's path
  """
  day_number = 1
  halt = 2
  start = 3
  finish = 4

def get_line_type(line: str) -> Optional[e_LineType]:
  """
  Returns category of a line

  >>> get_line_type("18:33 - 18:42 остановились на ручье, пополнить запасы воды")
  <e_LineType.halt: 2>
  """
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
  """
  Counts and returns CH H V for appropriately formatted report.

  >>> get_ch_h_v(["День 1", \
  "Погода тёплая, дежурные встали в 3:35, общий подъём в 4:40, настроение группы хорошее.", \
  "9:20 вышли на маршрут.", \
  "приближается дождь", \
  "10:00 - 10:10 привал технический, надеваем дождевики", \
  "10:30 - 10:37 привал технический, надеваем дождевики", \
  "10:40 начался дождь", \
  "11:11 встали, решили сделать днёвку. +15 градусов"], \
  True)
  <BLANKLINE>
  День 1
  0:10:00
  0:17:00
  День 1 ЧХВ = 11:11 - 9:20 - 0:17 = 1:34
  """

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