'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''


def p_tags(some_func):
    def wrapper(text, tag):
        new_text = f"<{tag}>{some_func(text)}</{tag}>"
        return new_text
    return wrapper


@p_tags
def body_text(message):
    return f"This is my message: {message}"


print(body_text("Barcelona is home to football team F.C. Barcelona.", "b"))
