from textnode import TextNode, TextType


def main():
    node = TextNode('some text', TextType.TEXT, 'https://NightHunters.com')
    print(node)


if __name__ == "__main__":
    main()