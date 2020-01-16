import csv
formats= {}
with open('formats.csv') as infile:
    formatReader=csv.reader(infile)
    for formatName, formatCode in formatReader:
        formatCodeInt = int(formatCode)
        formats[formatCodeInt] = [formatName]

print(formats)
