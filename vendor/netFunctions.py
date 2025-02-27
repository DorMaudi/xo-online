import zlib

def wrap(data):
    wrp = zlib.compress(data.encode('utf-8'), 3)
    #print("compressed:", wrp)
    return wrp

def unwrap(data):
    uwrp = zlib.decompress(data)
    #print("unwarped:", uwrp)
    return uwrp

# if __name__ == '__main__':
#     h = wrap("my name is dor")
#     unwrap(h)