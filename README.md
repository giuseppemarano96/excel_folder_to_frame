```python
from numpy import nan
import excel_folder_to_frame

col_to_delete = ['NOME', 'NOTE', 'EXTRA']

source = Folder('documents/')
document = source.get_melter(index='ID', rimuovi=col_to_delete)
strings = extract_non_integers(document.value.dropna())

for x in strings:
    document.value = document.value.replace(strings, nan)

print(document.fillna(0))