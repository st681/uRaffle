import csv
import json

class readTasks:
    def __init__(self, csv_file, processor):
        self.csv_file = csv_file
        self.processor = processor

    async def processEntries(self):
        with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                requiredFields = self.processor.requiredFields()
                filteredData = {k: v for k, v in row.items() if k in requiredFields}
                await self.processor.process(filteredData)