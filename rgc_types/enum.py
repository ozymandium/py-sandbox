#!/usr/bin/env python

def enum(*args, **kwargs):
    """
    In [2]: a = enum('x', 'y', 'z')

    In [3]: a.x
    Out[3]: 0

    In [4]: a.y
    Out[4]: 1

    In [5]: a.z
    Out[5]: 2

    In [5]: a.reverse[0]
    Out[5]: 'x'

    In [6]: a.reverse[1]
    Out[6]: 'y'

    """
    enums = dict(zip(args, range(len(args))), **kwargs)

    # support for converting back
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse'] = reverse

    return type('Enum', (), enums)

################################################################################

## {{{ http://code.activestate.com/recipes/67107/ (r1)
import types, string, pprint, exceptions

class EnumException(exceptions.Exception):
    pass

class Enumeration:
    def __init__(self, name, enumList):
        self.__doc__ = name
        lookup = { }
        reverseLookup = { }
        i = 0
        uniqueNames = [ ]
        uniqueValues = [ ]
        for x in enumList:
            if type(x) == types.TupleType:
                x, i = x
            if type(x) != types.StringType:
                raise EnumException, "enum name is not a string: " + x
            if type(i) != types.IntType:
                raise EnumException, "enum value is not an integer: " + i
            if x in uniqueNames:
                raise EnumException, "enum name is not unique: " + x
            if i in uniqueValues:
                raise EnumException, "enum value is not unique for " + x
            uniqueNames.append(x)
            uniqueValues.append(i)
            lookup[x] = i
            reverseLookup[i] = x
            i = i + 1
        self.lookup = lookup
        self.reverseLookup = reverseLookup
    def __getattr__(self, attr):
        if not self.lookup.has_key(attr):
            raise AttributeError
        return self.lookup[attr]
    def whatis(self, value):
        return self.reverseLookup[value]

"""Volkswagen = Enumeration("Volkswagen",
    ["JETTA",
     "RABBIT",
     "BEETLE",
     ("THING", 400),
     "PASSAT",
     "GOLF",
     ("CABRIO", 700),
     "EURO_VAN",
     "CLASSIC_BEETLE",
     "CLASSIC_VAN"
     ])

Insect = Enumeration("Insect",
    ["ANT",
     "APHID",
     "BEE",
     "BEETLE",
     "BUTTERFLY",
     "MOTH",
     "HOUSEFLY",
     "WASP",
     "CICADA",
     "GRASSHOPPER",
     "COCKROACH",
     "DRAGONFLY"
     ])

def demo(lines):
    previousLineEmpty = 0
    for x in string.split(lines, "\n"):
        if x:
            if x[0] != '#':
                print ">>>", x; exec x; print
                previousLineEmpty = 1
            else:
                print x
                previousLineEmpty = 0
        elif not previousLineEmpty:
            print x
            previousLineEmpty = 1

def whatkind(value, enum):
    return enum.__doc__ + "." + enum.whatis(value)

class ThingWithType:
    def __init__(self, type):
        self.type = type
"""
# demo("""
# car = ThingWithType(Volkswagen.BEETLE)
# print whatkind(car.type, Volkswagen)
# bug = ThingWithType(Insect.BEETLE)
# print whatkind(bug.type, Insect)

# # Notice that car's and bug's attributes don't include any of the
# # enum machinery, because that machinery is all CLASS attributes and
# # not INSTANCE attributes. So you can generate thousands of cars and
# # bugs with reckless abandon, never worrying that time or memory will
# # be wasted on redundant copies of the enum stuff.

# print car.__dict__
# print bug.__dict__
# pprint.pprint(Volkswagen.__dict__)
# pprint.pprint(Insect.__dict__)
# """)
## end of http://code.activestate.com/recipes/67107/ }}}


