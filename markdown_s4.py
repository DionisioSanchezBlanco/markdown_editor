# Stage 2
options = {
    "!done": "!done",
    "!help": "!help",
    "plain": "plain",
    "bold": "bold",
    "italic": "italic",
    "inline-code": "inline-code",
    "link": "link",
    "header": "header",
    "unordered-list": "unordered-list",
    "ordered-list": "ordered-list",
    "line-break": "line-break"
    }
list_text = []

class Mark:
    def __init__(self, options):
        self.options = options

    def check_option(self, choose):
        if choose not in self.options:
            print("Unknown formatting type or command. Please try again")
        elif self.options[choose] == "!help":
            print("Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break")
            print("Special commands: !help !done")
        elif self.options[choose] == 'header':
            list_text.append(mark.header_format())
        elif self.options[choose] == 'plain':
            list_text.append(mark.plain_format())
        elif self.options[choose] == 'link':
            list_text.append(mark.url_format())
        elif self.options[choose] == 'bold':
            list_text.append(mark.bold_format())
        elif self.options[choose] == 'italic':
            list_text.append(mark.italic_format())
        elif self.options[choose] == 'line-break':
            list_text.append(mark.break_format())
        elif self.options[choose] == 'inline-code':
            list_text.append(mark.code_format())
        elif self.options[choose] == 'ordered-list':
            mark.ordered_format()
        elif self.options[choose] == 'unordered-list':
            mark.ordered_format(False)
        else:
            pass

# Ordered and unordered lists can be coded in one method
    def ordered_format(self, order=True):
        rows = 0
        while rows <= 0:
            rows = int(input("Number of rows: "))
            if rows <= 0:
                print("The number of rows should be greater than zero")
            else:
                for i in range(1, rows + 1):
                    element = input(f"Row #{i}: ")
                    if order:
                        list_text.append(f"{i}. {element}\n")
                    else:
                        list_text.append(f"* {element}\n")

    def header_format(self):
        level = int(input("Level: "))
        if level not in range(1, 7):
            return "The level should be within the range of 1 to 6"
        else:
            text_header = input("Text: ")
            symbol = "#" * level
            return f"{symbol} {text_header}\n"

    def plain_format(self):
        return input("Text: ")

    def url_format(self):
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"

    def code_format(self):
        return f"`{input('Text: ')}`"

    def italic_format(self):
        return f"*{input('Text: ')}*"

    def bold_format(self):
        return f"**{input('Text: ')}**"

    def break_format(self):
        return "\n"

mark = Mark(options)
choose = input("- Choose a formatter: ")

while choose != "!done":   
    mark.check_option(choose)
    #print(''.join(list_text))
    print(''.join(list_text))
    choose = input("- Choose a formatter: ")
