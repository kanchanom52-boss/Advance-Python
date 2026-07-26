def decorate_report(fun):
    def wrapper(*args):
        print("********************")
        fun(*args)
        print("********************")
    return wrapper

class Report:
    template = "Default Template"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, new_template):
        cls.template = new_template

    def __str__(self):
        return (
            "Template: " + self.template + "\n" +
            "Title: " + self.title + "\n" +
            "Content: " + self.content
        )

    @decorate_report
    def show_report(self):
        print(self)

Report.change_template("Student Report")
r1 = Report("Python Project", "Dynamic Report Generator using OOP")
r1.show_report()
