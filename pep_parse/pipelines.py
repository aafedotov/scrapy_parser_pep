import csv
import datetime as dt

from collections import defaultdict
from pathlib import Path


class PepParsePipeline:

    def __init__(self):

        super(PepParsePipeline, self).__init__()
        self.pep_count = 0
        self.status_count = defaultdict(int)

    def open_spider(self, spider):

        results_dir = Path(__file__).parent.parent / 'results'
        results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):

        self.pep_count += 1
        self.status_count[item['Статус']] += 1
        return item

    def close_spider(self, spider):

        results = [('Статус', 'Количество')]
        results.extend([status for status in self.status_count.items()])
        results.append(('Total', self.pep_count))

        now = dt.datetime.now()
        now_formatted = now.strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = Path(__file__).parent.parent / 'results' / file_name

        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
