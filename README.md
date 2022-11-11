# ch_h_v

Cкрипт для подсчёта чистого ходового времени из текстового (txt) файла с отчётом.

Скрипт принимает во внимание только строчки следующего вида:

```
Обозначение дня:
День N

Время выхода на маршрут и остановки на ночлег:
__:__ вышли (на маршрут ...)
__:__ встали (на ужин, на ночёвку, на месте ночёвки ...)

Привалы/остановки:
__:__ - __:__ привал (привал технический ...)
__:__- __:__ остановились/остановка (на обед, на ручье пополнить запасы воды, у пещеры ...)
```

Остальные строчки могут быть любыми.

Аргументы:
  -h, --help            помощь
  -f FILENAME, --filename FILENAME
                        Файл с отчётом
  -v, --verbose         Вывод промежуточных значений. Может пригодиться для проверки правильности работы скрипта.

Пример запуска: `python ch_h_v.py --filename="Пример отчёта.txt" -v`
Пример отчёта лежит в репозитории.
Пример дня. Жирным выделены слова, которые скрипт примет во внимание для рассчёта ЧХВ

> **День N**  
> Погода тёплая, дежурные встали в 3:35, общий подъём в 4:40, настроение группы хорошее.  
> **5:20 вышли** на маршрут.  
> приближается дождь  
> **6:00 - 6:10 привал** технический, надеваем дождевики  
> 6:15 начался дождь  
> ...  
> **12:20 - 12:31 остановились** на ручье пополнить запасы воды.  
> 12:41 - 13:02 прошли реку вброд  
> Прошли старый кош, дождь + туман 30м видимость  
> **13:20 - 13:25 привал**  
> **14:01 - 14:06 привал**. Видели лося вдалеке.  
> ...  
> **16:40 - 17:00 остановка** у пещеры. Сделали несколько фотографий.  
> **17:20 встали** на ночёвку +15 градусов  
>  
> Ветер тек широкой, ровной волной, но иногда он точно прыгал через что-то невидимое и, рождая сильный порыв, развевал волосы женщин в фантастические гривы, вздымавшиеся вокруг их голов. Это делало женщин странными и сказочными. Они уходили все дальше от нас, а ночь и фантазия одевали их все прекраснее.  
>  
> Кто-то играл на скрипке... девушка пела мягким контральто, слышался смех...  
> 
> Воздух был пропитан острым запахом моря и жирными испарениями земли, незадолго до вечера обильно смоченной дождем. Еще и теперь по небу бродили обрывки туч, пышные, странных очертаний и красок, тут — мягкие, как клубы дыма, сизые и пепельно-голубые, там — резкие, как обломки скал, матово-черные или коричневые. Между ними ласково блестели темно-голубые клочки неба, украшенные золотыми крапинками звезд. Все это — звуки и запахи, тучи и люди — было странно красиво и грустно, казалось началом чудной сказки. И все как бы остановилось в своем росте, умирало; шум голосов гас, удаляясь, перерождался в печальные вздохи.  
>  
> 19:50 отбой  
