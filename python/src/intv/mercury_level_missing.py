counter = 0
for row in open('myfile'):
    dt, value = row.split(sep='\t', max=2)
    if value.startswith('Missing'):
        print(value)
        counter += 1
        if counter == 20:
            break
