import re
import enum
from typing import Protocol
from typing import Optional

"""
Тут я решил применить Dependency Injection, чтобы
- Локализовать и обернуть код с regexp'ами в dependency,
  и облегчить будущую возможную его замену;
- Попрактиковаться в ООП;
- Попробовать реализовать паттерн DI на Python,
  где ещё нет именно интерфейсов (зато есть протоколы).
"""

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

class ILineParse(Protocol):
  """Interface for parsing lines"""
  def get_type(self, line: str) -> Optional[e_LineType]:
    """Returns category of a line"""
    raise NotImplementedError
  
class RegexpLineParser:
  """Parse lines via regexp"""

  def get_type(self, line: str) -> Optional[e_LineType]:
    """Returns category of a line"""
    regexes = {
    e_LineType.day_number: r"День \d{1,2}",
    e_LineType.halt: r"\d{1,2}:\d{2} - \d{1,2}:\d{2} (привал|остановились|остановка)",
    e_LineType.start: r"\d{1,2}:\d{2} (вышли)",
    e_LineType.finish: r"\d{1,2}:\d{2} (встали)"}

    for line_type in e_LineType:
        if re.match(regexes[line_type], line):
            return(line_type)
    
    return None

def get_line_type(line: str, line_parser: ILineParse) -> Optional[e_LineType]:
   """
    Returns category of a line

    >>> get_line_type( \
      "18:33 - 18:42 остановились на ручье, пополнить запасы воды", \
      RegexpLineParser())
    <e_LineType.halt: 2>
    """
   return line_parser.get_type(line)