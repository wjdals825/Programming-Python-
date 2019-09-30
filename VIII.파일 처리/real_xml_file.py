import xml.etree.ElementTree as ET


f = open("movie.xml", "r" , encoding="utf-8")
data = f.read()
# print(data)
tree = ET.ElementTree(ET.fromstring(data))
root = tree.getroot()
# print(root.tag)

for child in root:
    print("tag: " + child.tag , child.text)
f.close()