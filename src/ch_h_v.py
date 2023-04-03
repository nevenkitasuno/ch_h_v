from datetime import timedelta
from typing import List
from typing import Generator

import converters as cvt
from LineParse import e_LineType, get_line_type, RegexpLineParser

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

def get_ch_h_v(inp: List[str], verbose: bool) -> Generator[str, None, None]:
  """
  Counts and returns CH H V generator object for appropriately formatted report.
  """

  for line in inp:
    if get_line_type(line, RegexpLineParser()) == e_LineType.day_number:
      # day started
      day_line = line
      if (verbose):
        yield("\n{}".format(day_line))
    # halt time count
    if get_line_type(line, RegexpLineParser()) == e_LineType.start:
      time_start = cvt.str_to_datetime(line)
      halt_per_day = timedelta()
    if get_line_type(line, RegexpLineParser()) == e_LineType.halt:
      halt_per_day += get_halt_time(line)
      if (verbose): yield(str(halt_per_day))
    if get_line_type(line, RegexpLineParser()) == e_LineType.finish:
      # day finished
      time_finish = cvt.str_to_datetime(line)
      total_day_time = time_finish - time_start - halt_per_day
      if (verbose):
        yield(day_line + ' ЧХВ = '
              + cvt.datetime_to_str(time_finish)
              + ' - ' + cvt.datetime_to_str(time_start)
              + ' - ' + cvt.timedelta_to_str(halt_per_day)
              + ' = ' + cvt.timedelta_to_str(total_day_time))
      else:
        yield(day_line + ' ЧХВ = ' + cvt.timedelta_to_str(total_day_time))