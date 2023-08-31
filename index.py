import pandas as pd

df_books = pd.DataFrame({
    'book_id': [101, 102, 103],
    'title': ['Book A', 'Book B', 'Book C'],
    'author': ['Author1', 'Author2', 'Author3']
})

df_books.set_index('book_id', inplace=True)
print(df_books)
