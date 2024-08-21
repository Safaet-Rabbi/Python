def format_xml(xml):
    level = 0
    i = 0
    n = len(xml)   
    while i < n:
        if xml[i] == '<':
            if xml[i + 1] != '/':
                print(' ' * (2 * level) + xml[i:i+3])
                level += 1
                i += 3
            else:
                level -= 1
                print(' ' * (2 * level) + xml[i:i+4])
                i += 4
xml_input = input()
format_xml(xml_input)
