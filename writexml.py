import xml.etree.ElementTree as xml


def Generatexml(filename):
    root = xml.Element("customers")
    c1 = xml.Element("test")
    root.append(c1)
    type1 = xml.SubElement(c1, "place")
    type1.text = "uk"
    Amount = xml.SubElement(c1, "amount")
    Amount.text = "4500"
    tree = xml.ElementTree(root)
    with open(filename, "wb") as files:
        tree.write(files)


if __name__ == "__main__":
    Generatexml("conigure.xml")
