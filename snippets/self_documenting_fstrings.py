import datetime
import uuid

guid = uuid.uuid4()
file_name = 'example_document.csv'
created_at = datetime.datetime(2022, 7, 6)

file_info = f'{guid=}, {file_name=}, {created_at=}'

print(file_info)
