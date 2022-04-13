
def tex_lexer(text):
    STATUS_TEXT = 0
    STATUS_COMMENT = 1
    STATUS_MARCO = 2
    STATUS_WHITE_SPACE = 3
    STATUS_NEWLINE = 4

    status = STATUS_TEXT

    for i, t in enumerate(text):
        if status == STATUS_TEXT:
            if t == '\\':
                status = STATUS_MARCO
            elif t == '%':
                status = STATUS_COMMENT
            elif t == ' ' or t == '\t' or t == '\r':
                status = STATUS_WHITE_SPACE
            elif t == '\n':
                status = STATUS_NEWLINE
            else:
                yield (i, t)
