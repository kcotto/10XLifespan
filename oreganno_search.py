import csv


def searchoreganno(filename):
    with open(filename) as tsvfile:
        results = []
        reader = csv.reader(tsvfile, delimiter = '\t')
        for column in reader:
            row = ','.join(column)
            if column[4] == 'ITGA6' or len(results) == 0:
                results.append(row)
            else:
                if column[4] == 'CPXM1' or len(results) == 0:
                    results.append(row)
                else:
                    if column[4] == 'PKD2' or len(results) == 0:
                        results.append(row)
                    else:
                        if column[4] == 'LAPTM4B' or len(results) == 0:
                            results.append(row)
                        else:
                            if column[4] == 'SLC7A6' or len(results) == 0:
                                results.append(row)
                            else:
                                if column[4] == 'ELOVL6' or len(results) == 0:
                                    results.append(row)
    return results


def write_search_results(results, filename):
    with open(filename, 'w') as output:
        output.write('\n'.join(results))

results = searchoreganno('ORegAnno_Combined_2015.09.15.tsv')
write_search_results(results, 'output.tsv')
print(results)