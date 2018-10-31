# assertionUtils.py
# Useful functions providing complex assertion that can't be done with tavern

# from jsonpath_rw import jsonpath, parse


def extract_object(json, json_path):
    extracted = ''
    for attribute in json_path.split('.'):
        if extracted:
            extracted = extracted[attribute]
        elif attribute in json:
            extracted = json[attribute]
        else:
            return None
    return extracted


def check_length(response, json_path, length):
    print "## Function[", check_length.__name__, "]"
    len_json_obj = len(extract_object(response.json(), json_path))
    print "\tlength of json_path[", json_path, "] = ", len_json_obj
    print "\tlength to compare = ", eval(length)
    assert len_json_obj == eval(length)


def check_greater_than(response, json_path, value_to_compare):
    print "## Function[", check_greater_than.__name__, "]"
    object = extract_object(response.json(), json_path)
    if isinstance(object, int):
        print "\tvalue of json_path[", json_path, "] = ", object
        print "\tvalue to compare = ", eval(value_to_compare)
        assert object > eval(value_to_compare)
    else:
        print "\tlength of json_path[", json_path, "] = ", len(object)
        print "\tvalue to compare = ", eval(value_to_compare)
        assert len(object) > eval(value_to_compare)


def length(response, json_path):
    print "## Function[", length.__name__, "]"
    array = extract_object(response.json(), json_path)
    if array is not None:
        print "\tlength of array[", json_path, "] = ", len(array)
        return {'length': len(array)}
    print "\tlength of array[", json_path, "] = ", 0
    return 0


def equals(response, json_path, to_eval):
    to_return = False
    print "## Function[", equals.__name__, "]"
    try:
        value_of_obj = extract_object(response.json(), json_path)
        print "\tvalue of json_path[", json_path, "] = ", value_of_obj
        print "\tvalue to compare = ", eval(to_eval)
        to_return = value_of_obj == eval(to_eval)
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        to_return = value_of_obj == eval(to_eval)
    assert to_return
