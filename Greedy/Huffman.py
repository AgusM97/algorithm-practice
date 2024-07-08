class Node:
    def __init__(self, value, freq, left, right) -> None:
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right


print("Text to encode:")
text = input()
freq = {}
for c in text:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
nodeList: list[Node] = []
for item in freq.items():
    nodeList.append(Node(item[0], item[1], None, None))
nodeList.sort(key=lambda node: node.freq, reverse=True)
while len(nodeList) > 1:
    x = nodeList.pop()
    y = nodeList.pop()
    z = Node(None, x.freq + y.freq, x, y)
    nodeList.append(z)
    nodeList.sort(key=lambda node: node.freq, reverse=True)
root = nodeList[0]


def generateCodes(codeDict: dict, node: Node, code: str):
    if node.value is None:
        generateCodes(codeDict, node.left, code + "0")
        generateCodes(codeDict, node.right, code + "1")
    else:
        codeDict[node.value] = code


codeDict = {}
generateCodes(codeDict, root, "")
codedText = ""
for c in text:
    codedText += f"{codeDict[c]}"
print(f"Huffman dictionary: {codeDict}")
print(f"Encoded text: {codedText}")
