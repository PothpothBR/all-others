def clear_spaces(buffer: str):  # formata o buffer

    if buffer[-1] == '\n':  # remove a quebra de linha
        buffer = buffer[:-1]

    for i in buffer:  # remove espacos antes
        if i == ' ':
            buffer = buffer[1:]
        else:
            break

    for i in range(len(buffer)):  # remove espacos depois
        if buffer[-1] == ' ':
            buffer = buffer[:-1]
        else:
            break

    return buffer  # retorn o buffer formatado


def clear_spaces_after(buffer: str):  # formata o buffer

    if buffer[-1] == '\n':  # remove a quebra de linha
        buffer = buffer[:-1]

    for i in buffer:  # remove espacos antes
        if i == ' ':
            buffer = buffer[1:]
        else:
            break

    return buffer  # retorn o buffer formatado


def clear_spaces_before(buffer: str):  # formata o buffer

    if buffer[-1] == '\n':  # remove a quebra de linha
        buffer = buffer[:-1]

    for i in range(len(buffer)):  # remove espacos depois
        if buffer[-1] == ' ':
            buffer = buffer[:-1]
        else:
            break

    return buffer  # retorn o buffer formatado


def format_spaces(buffer: str) -> str:
    for i in range(len(buffer)):  # remove espacos extras antes
        if buffer[i] == ' ':
            if buffer[i + 1] == ' ':
                buffer = buffer[1:]
        else:
            break

    for i in range(len(buffer)):  # remove espacos extras depois
        if buffer[-1] == ' ':
            if buffer[-2] == ' ':
                buffer = buffer[:-1]
        else:
            break

    return buffer  # retorna o buffer formatado


def format_spaces_after(buffer: str) -> str:
    for i in range(len(buffer)):  # remove espacos extras antes
        if buffer[i] == ' ':
            if buffer[i + 1] == ' ':
                buffer = buffer[1:]
        else:
            break

    return buffer  # retorna o buffer formatado


def format_spaces_before(buffer: str) -> str:

    for i in range(len(buffer)):  # remove espacos extras depois
        if buffer[-1] == ' ':
            if buffer[-2] == ' ':
                buffer = buffer[:-1]
        else:
            break

    return buffer  # retorna o buffer formatado

