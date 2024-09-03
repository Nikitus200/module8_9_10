def all_variants(text):
    for _ in text:
        yield _
    for j in range(len(text) - 1):
        y = text[j]
        for g in range(j + 1, len(text)):
            y = y + text[g]
            yield y
a = all_variants("abc")
for i in a:
    print(i)