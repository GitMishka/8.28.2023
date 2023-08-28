import csv

# Open the source and destination CSV files
with open('data.csv', 'r') as source, open('filtered_data.csv', 'w', newline='') as dest:
    # Initialize CSV reader and writer
    reader = csv.DictReader(source)
    writer = csv.DictWriter(dest, fieldnames=reader.fieldnames)

    # Write the header to the destination file
    writer.writeheader()

    # Filter and write rows
    for row in reader:
        if row['country'] != 'USA':
            writer.writerow(row)
