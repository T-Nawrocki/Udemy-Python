# An HTML document is COMPOSED of three components:
#   (1) a line containing the  HTML version information;
#   (2) a declarative HEAD section; and
#   (3) a BODY section, containing the actual content of the document.

# So we know that composition would be a good way to represent and handle HTML in python.


class Tag:

    def __init__(self, name, contents):
        self.start_tag = f"<{name}>"
        self.end_tag = f"</{name}>"
        self.contents = contents

    def __str__(self):
        return f"{self.start_tag}{self.contents}{self.end_tag}"

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', "")
        self.end_tag = ""  # DOCTYPE doesn't have an end tag


class Head(Tag):

    # We're not going to get distracted for now—Header contents will be empty—but might change this in a challenge.
    def __init__(self):
        super().__init__("HEAD", "")


class Body(Tag):

    def __init__(self):
        super().__init__("BODY", "")  # body contents start empty, but are built up separately
        self._body_contents = []

    # An example of composition—Body objects are composed of a set of other Tag objects
    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)


# This is our main example of Composition—the HTML Doc is composed of a DocType, a Head, and a Body
# none of which are subclasses of HtmlDoc (and nor should they be, given that they share very few if any properties).
# Here, the class is entirely composed of other classes, but that doesn't have to be the case.
class HtmlDoc:

    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    # Delegating display of the components to the component classes themselves.
    # By calling this method "display", it corresponds to the method in each of the component classes.
    # It can therefore also be used by any function that displays Tag objects (example of polymorphism).
    # In fact, the methods of this class are the same as the methods of the Body class, so any function which
    # can take a Body argument can also take an HtmlDoc as an argument
    # (meaning we've built a kind of recursion into our program,
    # where each HtmlDoc can be the Body of another HtmlDoc and so on.)
    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<HTML>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</HTML>", file=file)


if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag("H1", "Main heading")
    my_page.add_tag("H2", "Subheading")
    my_page.add_tag("P", "This is a paragraph which will appear on the page.")
    my_page.add_tag("P", "This is another paragraph which will appear on the page.")
    with open("test.html", "w") as test_doc:
        my_page.display(file=test_doc)
