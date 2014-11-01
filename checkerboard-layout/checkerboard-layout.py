#!/usr/bin/env python


def template(title, styles, wordlist):
    return """<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <title>{0}</title>
  <style>{1}</style>
</head>
<body>{2}</body>
""".format(title, '\n'.join(styles), ''.join(wordlist))


def main(argv):
    words = []
    with open(argv[1], 'r') as f:
        for line in f:
            words.extend(line.strip().replace('-', ':').split())

    styles = [
        ".b0 { background: black; color: white; word-wrap: break-word }",
        ".b1 { background: white; color: black; word-wrap: break-word }",
    ]

    title = "Gimme that Old-Time Collision"

    num = 0
    marked_up_words = []
    for word in words:
        marked_up_words.append(
            '<span class="b{0}">{1}</span>'.format(num % 2, word)
        )
        num += 1

    print template(title, styles, marked_up_words)


if __name__ == '__main__':
    import sys
    main(sys.argv)
