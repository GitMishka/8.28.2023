import csv

def read_csv_in_batches(filename, batch_size=1000):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        batch = []
        for row in reader:
            if len(batch) == batch_size:
                yield batch
                batch = []
            batch.append(row)
        if batch:
            yield batch

for batch in read_csv_in_batches('big_data.csv'):
    # Process each batch of 1000 rows
    pass
