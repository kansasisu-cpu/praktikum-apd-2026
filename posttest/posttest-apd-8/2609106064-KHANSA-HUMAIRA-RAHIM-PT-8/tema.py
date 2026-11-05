from blessed import Terminal
from inquirer.themes import Default

term = Terminal()


class tema_awal(Default):
    def __init__(self):
        super().__init__()
        self.List.selection_cursor = "➜"
        self.List.selection_color = term.pink
        self.List.unselected_color = term.normal
        self.Question.mark_color = term.bold_pink
        self.Question.brackets_color = term.bright_black


class tema_admin(Default):
    def __init__(self):
        super().__init__()
        self.List.selection_cursor = "➜"
        self.List.selection_color = term.skyblue
        self.List.unselected_color = term.normal
        self.Question.mark_color = term.bold_skyblue
        self.Question.brackets_color = term.bright_black


class tema_user(Default):
    def __init__(self):
        super().__init__()
        self.List.selection_cursor = "➜"
        self.List.selection_color = term.darkseagreen
        self.List.unselected_color = term.normal
        self.Question.mark_color = term.bold_darkseagreen
        self.Question.brackets_color = term.bright_black