import csv
import datetime as dt

from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def __init__(self):
        """Конструктор. Создаем счетчики статусов."""

        super(PepParsePipeline, self).__init__()
        self.pep_count = 0
        self.status_count = defaultdict(int)

    def open_spider(self, spider):
        """Создаем папку для результатов, если ее нет."""

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        """Считаем статусы."""

        if item['status']:
            self.pep_count += 1
            self.status_count[item['status']] += 1
        return item

    def close_spider(self, spider):
        """Записываем результаты в csv-файл."""

        results = [('Статус', 'Количество')]
        results.extend([status for status in self.status_count.items()])
        results.append(('Total', self.pep_count))

        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = BASE_DIR / 'results' / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
