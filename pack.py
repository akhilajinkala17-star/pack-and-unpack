#1.
def pack_data(*n):
    print(n)
pack_data(1,2,3,4,5)

#2.
def unpack_data(*n):
    a,b,c,d,e=n
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
unpack_data(1,2,3,4,5)

#3.
def pack_data(*args):
    print("Packed:", args)
    return args


def unpack_data(data):
    for value in data:
        print("Unpacked:", value)


def process_data(*args):
    packed_data = pack_data(*args)
    unpack_data(packed_data)


process_data(10, 20, 30)

process_data(1.3, 4.5, 3.6)

process_data("python", "java")

