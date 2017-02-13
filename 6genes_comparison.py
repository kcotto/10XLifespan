import csv

def generate_filelist(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content]


def count_genes(counts, filename, index, max_index):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            key = line[0].upper()
            new_value = int(line[1])
            if key in counts:
                cur_value = counts[key]
                cur_value[0] += new_value
                cur_value[index + 1] += new_value
            else:
                cur_value = [0] * (max_index + 1)
                cur_value[0] = new_value
                cur_value[index + 1] = new_value
                counts[key] = cur_value


dict = {}

files = generate_filelist('6genefiles_200.txt')
header = []
header.append('Gene name')
header.append('Total count')
for idx, file in enumerate(files):
    header.append(file)
    count_genes(dict, file, idx, len(files))

with open('gene_counts.csv', 'w') as output:
    output.write(','.join(header) + '\n')
    for key in dict.keys():
        output.write('{0},{1}'.format(key, ','.join([str(value) for value in dict[key]])) + '\n')