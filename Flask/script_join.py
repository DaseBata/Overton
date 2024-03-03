import jsonlines
import os

data = []

folder_path = 'data'
for filename in os.listdir(folder_path):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(folder_path, filename)
        with jsonlines.open(file_path) as reader:
            data.extend(reader.iter(type=dict, skip_invalid=True))

merged_file_path = 'overton.jsonl'
with jsonlines.open(merged_file_path, mode='w') as writer:
    writer.write_all(data)
