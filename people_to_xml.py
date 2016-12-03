import sys
from pprint import pprint as pp


def get_people():
    # get the people
    people = {}
    file_handler = open("d:\dev\people.txt", "r")
    for person_info in file_handler:
        person = person_info.split()
        # print(person)
        people[person[0]] = person[1:3]

    return people


def build_people_xml(people):
    people_xml_string = '<?xml version="1.0" encoding="utf-16"?>\n<people>\n'

    for person_id in people:
        person = {'id': person_id, 'first_name': people[person_id][0], 'last_name': people[person_id][1]}
        people_xml_string += build_person_xml(person)

    people_xml_string += '</people>\n'
    return people_xml_string


def build_person_xml(person):
    person_xml_string = ' ' * 2 + '<person>' + '\n'
    person_xml_string += ' ' * 4 + '<id>' + person['id'] + '</id>' + '\n'
    person_xml_string += ' ' * 4 + '<first_name>' + person['first_name'] + '</first_name>' + '\n'
    person_xml_string += ' ' * 4 + '<last_name>' + person['last_name'] + '</last_name>' + '\n'
    person_xml_string += ' ' * 2 + '</person>' + '\n'
    return person_xml_string

def main(argv):
    people = get_people()
    # pp(build_people_xml(people))
    print(build_people_xml(people))
    #pp(people)


if __name__ == '__main__':
    main(sys.argv)
