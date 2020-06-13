file_src, file_dst = './README.md', './README_CLEAN.md'
clean_words = ['**Key Points**', '**Dataset**']

with open(file_src, 'r') as f:
    lines = f.readlines()

with open(file_dst, 'w') as f:
    for line in lines:
        # print([word in line.strip() for word in clean_words])
        if not any([word in line.strip() for word in clean_words]):
            f.write(line)