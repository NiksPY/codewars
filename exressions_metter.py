def expression_matter(a, b, c):
    first = a * (b+c)
    second = a * b * c
    third = a + b * c
    fourth = (a + b) * c
    fifth = a + b + c
    sixth = a * b + c
    l = [first, second, third, fourth, fifth, sixth]
    return max(l)