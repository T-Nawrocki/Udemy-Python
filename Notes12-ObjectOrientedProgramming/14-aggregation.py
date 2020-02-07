# AGGREGATION is very similar to composition, and is often described as a weaker form of composition.

# With composition, the objects that another object is composed of do not exist outside of their container.
# So in our previous HTML example, the DocType, Head and Body objects which compose the HtmlDoc
# are only used in the HtmlDoc class, so objects of those types will never exist except as part of an HtmlDoc.
# When the HtmlDoc is deleted, the DocType, Head and Body objects it is composed of are also deleted.

# To note—we have marked the attributes of HtmlDoc as non-public (_doc_type, _head, _body).
# In other programming languages, this would mean that we need to change the HtmlDoc class
# in order to make this program use aggregation rather than composition.
# However as we know, in Python there isn't really a true "private" state, so really
# the line between aggregation and composition can get quite blurred.
# So the important thing is instead to look at the intent behind the code, rather than restrictions in the code itself.


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
    def __init__(self, title=None):
        super().__init__("HEAD", "")
        if title is not None:
            self.contents = str(Tag("TITLE", title))


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


class HtmlDoc:

    def __init__(self, title=None):
        self._doc_type = DocType()
        self._head = Head(title)
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print("<HTML>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print("</HTML>", file=file)


if __name__ == '__main__':
    my_page = HtmlDoc("Document title")
    my_page.add_tag("H1", "Main heading")
    my_page.add_tag("H2", "Subheading")
    my_page.add_tag("P", "This is a paragraph which will appear on the page.")
    my_page.add_tag("P", "This is another paragraph which will appear on the page.")
    with open("test.html", "w") as test_doc:
        my_page.display(file=test_doc)

    new_body = Body()
    new_body.add_tag("H1", "Aggregation!")
    new_body.add_tag("P", "Unlike <strong>composition</strong>, aggregation uses existing instances"
                          " of objects to build up another object.")
    new_body.add_tag("P", "The composed object doesn't actually own the objects that it's composed of."
                          " If it's destroyed, those objects continue to exist.")

    my_page._body = new_body
    with open("test2.html", "w") as test_doc:
        my_page.display(file=test_doc)