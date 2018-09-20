import os

file_paths = list()


def walk(dirname, ext):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            if ext in path:
                file_paths.append(path)
                txt_to_html(path, ext)
        else:
            walk(path, ext)
    return file_paths


def txt_to_html(path, ext):
    with open(path, "r") as f:
        title = f.readline().strip()
        body = ""
        for lines in f:
            body += f"<p>{lines.strip()}</p>"
        page = f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
</head>
<body>
    <h1>{title}</h1>
    {body}
</body>
</html>"""
    with open(path.replace(ext, ".html"), "w") as fout:
        fout.write(page)


cwd = os.getcwd()
print(walk(cwd, ".txt"))
