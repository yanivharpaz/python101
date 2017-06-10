from lxml import etree

data_dict = {"file1":
                {"sug": 1,
                 "name": "limor",
                 "lastname": "levi"
                 },
             "file2":
                 {"sug": 2,
                 "name": "yaniv",
                 "lastname": "harpaz"
                 },
             "file3":
                 {"sug": 3,
                  "name": "adi",
                  "lastname": "caspi"
                  },
           }

for filename,value in data_dict.items():
        print(filename)
        print(value)
        root = etree.Element("root", code="clalit")
        etree.SubElement(root, "sug").text = str(value['sug'])
        etree.SubElement(root, "name").text = value['name']
        etree.SubElement(root, "lastname").text = value['lastname']
        print(etree.tostring(root, pretty_print=True))
        print('T:\\Users\\yaniv\\GoogleDrive\\limor\\python\\'+filename+'.xml')
        outFile = open('T:\\Users\\yaniv\\GoogleDrive\\limor\\python\\'+filename+'.xml', 'wb')
        outFile.write(etree.tostring(root, pretty_print=True))
        outFile.close()

