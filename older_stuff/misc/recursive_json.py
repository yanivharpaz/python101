from json import dumps, loads
from pprint import pformat as pf, pprint as pp

def get_json():
    result = """
    {"counter":
        {"counterGroup":
            {"counter1":
                {"id": 111
                ,"name": "my_name"
                ,"counterValue": 50
                },
             "counter2":
                {"id": 112
                ,"name": "my_name2"
                ,"counterValue": 770
                }

            }
        }
    }
    """
    return result

def get_name_and_value(dict_to_parse):
    for key, value in dict_to_parse.items():
        print("-*" * 8)
        print("key:", key, "value:", value, "dict:", dict_to_parse)
        if key == "id":
            result_key = dict_to_parse['name']
            result_value = value
            result_tuple = (result_key, result_value)
            yield result_tuple
        elif isinstance(value, dict):
            for id_val in get_name_and_value(value):
                yield id_val
        # return result_tuple



def main():
    print("hi")
    x_x = get_json().strip()
    my_str = pf(x_x)
    my_dict = loads(x_x)
    my_str = dumps(my_dict, indent=2).strip()
    print(my_dict['counter']['counterGroup'])
    # pp(my_str)
    for _ in get_name_and_value(my_dict):
        print(_)


if __name__ == "__main__":
    main()