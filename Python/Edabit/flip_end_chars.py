def flip_end_chars(txt):
    if isinstance(txt, str):
        a = 'STR'
    else:
        return "Incompatible."
    if len(txt) < 2:
        return "Incompatible."
    s = list(txt)
    txtf = txt[0]
    txtl = txt[-1]
    if txtf == txtl:
        return "Two's a pair."
    s[0] = txtl
    s[-1] = txtf
    ns = "".join(s)

    return ns

flip_end_chars('saab')