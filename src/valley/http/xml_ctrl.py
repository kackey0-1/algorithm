import xml.etree.ElementTree as ET


if __name__ == '__main__':
    # root = ET.Element('root')
    # tree = ET.ElementTree(element=root)
    #
    # employee = ET.SubElement(root, 'employee')
    #
    # employ = ET.SubElement(employee, 'employ')
    # employ_id = ET.SubElement(employ, 'id')
    # employ_id.text = '111'
    # employ_name = ET.SubElement(employ, 'name')
    # employ_name.text = 'Mike'
    #
    # employ = ET.SubElement(employee, 'employ')
    # employ_id = ET.SubElement(employ, 'id')
    # employ_id.text = '222'
    # employ_name = ET.SubElement(employ, 'name')
    # employ_name.text = 'Ken'
    #
    # tree.write('data/tests.xml', encoding='utf-8', xml_declaration=True)

    tree = ET.ElementTree(file='data/test.xml')
    root = tree.getroot()

    for employee in root:
        for employ in employee:
            for person in employ:
                print(person.tag, person.text)
