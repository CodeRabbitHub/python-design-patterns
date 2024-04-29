# Flyweight factory
class FontStyleFactory:
    _styles = {}

    @staticmethod
    def get_style(style):
        if style not in FontStyleFactory._styles:
            FontStyleFactory._styles[style] = FontStyle(style)
        return FontStyleFactory._styles[style]


# Flyweight
class FontStyle:
    def __init__(self, style):
        self.style = style

    def apply(self, text):
        return f"{self.style} {text}"


# Client
class TextEditor:
    def __init__(self):
        self.texts = []

    def add_text(self, content, style):
        style_obj = FontStyleFactory.get_style(style)
        self.texts.append((content, style_obj))

    def display(self):
        for text, style in self.texts:
            print(style.apply(text))


# Example usage
editor = TextEditor()
editor.add_text("Hello", "bold")
editor.add_text("world", "italic")
editor.add_text("!", "underline")
editor.add_text("Welcome", "bold")
editor.add_text("to", "italic")
editor.add_text("Flyweight", "bold")

editor.display()
