from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in ["br", "hr", "img", "input", "link", "meta", "source", "area", "base", "col", "embed", "keygen", "param", "track", "wbr"]:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag not in ["br", "hr", "img", "input", "link", "meta", "source", "area", "base", "col", "embed", "keygen", "param", "track", "wbr"]:
            if not self.stack:
                print(f"Error: Unexpected end tag </{tag}> at {self.getpos()}")
                return
            start_tag, pos = self.stack.pop()
            if start_tag != tag:
                print(f"Error: Mismatched tag </{tag}> at {self.getpos()} (expected </{start_tag}> from {pos})")

    def close(self):
        super().close()
        for tag, pos in reversed(self.stack):
            print(f"Error: Unclosed tag <{tag}> at {pos}")

parser = MyHTMLParser()
with open("formaciones.html", "r") as f:
    parser.feed(f.read())
parser.close()
