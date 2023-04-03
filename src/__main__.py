import argparse
import sys

from ch_h_v import get_ch_h_v

def get_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(
                      prog = 'ch_h_v',
                      description = 'Скрипт для подсчёта чистого ходового времени из текстового файла с отчётом',
                      epilog = 'Файл должен быть нужного формата, см. README.md')

  parser.add_argument('-f', '--filename', help="Файл с отчётом")
  parser.add_argument('-v', '--verbose', action='store_true', help="Вывод промежуточных значений. Может пригодиться для проверки.")

  args = parser.parse_args()

  return (args)

def main() -> None:
  
  args = get_args()

  if (not args.filename):
    content = sys.stdin.read().splitlines()
  else:
    with open(args.filename) as f:
      content = f.read().splitlines()
  
  result_generator = get_ch_h_v(content, args.verbose)

  for outp in result_generator:
    print(outp)

if __name__ == '__main__':
  main()