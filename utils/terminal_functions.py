def yes_or_no(question):
    reply = str(input(question+' (y/N): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'N':
        return False
    else:
        return yes_or_no("Wrong Input." + question)


def update_terminal_question(update):
    def wrapped(question):
        return update or yes_or_no(question)
    return wrapped