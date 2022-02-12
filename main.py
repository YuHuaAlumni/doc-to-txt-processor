import re
from io import StringIO

from docx import Document

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = []
    f = open('list.docx', 'rb')
    document = Document(f)
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                txt = cell.text
                if txt and not txt.isspace():
                    txt = ' '.join(txt.split())
                    txt = txt.replace("校 友", "校友")
                    data.append(txt)
    f.close()

    with open('process.txt', 'w') as f:
        for line in data:
            f.write(line)
            f.write("\n")


