def justify(text, width):
    result, current, line_length, line = [], [], 0, text.split(' ')
    for word in line:
        if line_length + len(current) + len(word) > width:
            result.append(add_spaces(current, width, line_length))
            current = []
            line_length = 0
        current.append(word)
        line_length += len(word)
    if len(current):
        result.append(add_spaces(current, width, line_length))

    return result

def add_spaces(current_line, width, line_length):
    if len(current_line) == 1:
        return current_line[0] + ' ' * (width - line_length)
    num_spaces = width - line_length
    space, remainder = divmod(num_spaces, len(current_line) - 1)
    for i in range(remainder):
        current_line[-2] += ' '
    return (' '  * space).join(current_line)
