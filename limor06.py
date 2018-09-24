def ex():

    try:
        2+"2"

    except Exception as e:
        print("bad "+e)


# ex()


def f():
    return g()


def g():
    returned = None
    try:
        returned = h()
    except Exception:
        print("caught")
    return returned


def h():
    raise Exception("arrgh")
f()



def connect_to_db(hostname):
    if