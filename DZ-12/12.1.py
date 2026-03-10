import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.readlines()

    inside_tag = False
    result = []
    for line in html:
        clean_line = ''
        for char in line:
            if char == '<':
                inside_tag = True
            elif char == '>':
                inside_tag = False
            elif not inside_tag:
                clean_line += char
        clean_line = clean_line.strip()
        if clean_line:
            result.append(clean_line)
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write('\n'.join(result))


delete_html_tags("draft.html")