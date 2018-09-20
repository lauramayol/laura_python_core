'''
Write a decorator function that wraps text passed to it in <p> tags.

'''


def p_tags(some_func):
    def wrapper(text):
        new_text = f"<p>{some_func(text)}</p>"
        return new_text
    return wrapper


@p_tags
def body_text(message):
    return f"This is my message: {message}"


print(body_text("Barcelona is home to football team F.C. Barcelona."))
