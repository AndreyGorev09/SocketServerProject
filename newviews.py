def index():
    with open('templates/index.html', 'r') as f:
        return f.read()

def page():
    with open('templates/page.html', 'r') as f:
        return f.read()
