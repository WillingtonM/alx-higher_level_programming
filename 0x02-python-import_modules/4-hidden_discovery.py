#!/usr/bin/python3
if __name__ == "__main__":
    '''Print names defined by hidden_4 modules'''
    import hidden_4

    hidden_names = dir(hidden_4)
    for name in hidden_names:
        if name[:2] != "__":
            print("{:s}".format(name))
