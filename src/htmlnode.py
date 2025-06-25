import unittest


class HtmlNode:
    def __init__(self, tag: str=None, value: str=None, children: list=None, props: dict=None ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError

    def props_to_html(self) -> str:
        res = ''
        if self.props:
            for key, value in self.props.items():
                res += f' {key}="{value}"'
        return res

    def __repr__(self) -> str:
        return f'HtmlNode({self.tag}, {self.value}, {self.children}, {self.props})'


class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if not self.value:
            raise ValueError('Empty node')
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.children:
            raise ValueError('No children in Parent node')
        if not self.tag:
            raise ValueError('No tag in Parent node')
        res = ''
        for child in self.children:
            res += child.to_html()

        return f'<{self.tag}>{res}</{self.tag}>'

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
