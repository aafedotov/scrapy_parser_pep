# Парсер документации PEP на фреймворке Scrapy.
### Финальный проект 19-го спринта курса Python+.
### Яндекс Практикум. 5-я когорта pythonplus.
### Студент: Андрей Федотов.

### Перед началом работы:
1. Склонируйте репозиторий.
2. Создайте виртуальное окружение.
3. Установите зависимости ```pip install -r requirements.txt```.

### Запуск парсера:
```
scrapy crawl pep
```

### Результаты работы парсера:
В корневом каталоге создается подкаталог results.
В ходе работы парсера в него выгружаются два csv-файла:
1. pep_%time.csv - список всех PEP  с номерами, названиями и статусами
2. status_summary_%time.csv - список всех статусов с их количеством.
