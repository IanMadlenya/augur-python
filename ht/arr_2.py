db=open('DB', 'w+r')
def address2int(address): return int(address.encode('hex'), 16)
def get_block(n):
    db.seek(n*64)
    return db.read(64)
def put_block(n, block):
    if len(block)>64: error()
    db.seek(n*64)
    return db.write(block)
def del_block(n):
    db.seek(n*64+60)
    db.write('\x00'*4)
def reserved_p(n):
    db.seek(n*64+60)
    t=db.read(4)
    if t=='': return False
    return address2int(t)!=0
first_empty=[0]
def first_empty_block(first_empty=first_empty):
    if reserved_p(first_empty[0]):
        first_empty=[-1]
        while True:
            first_empty[0]+=1
            if not reserved_p(first_empty[0]):
                return first_empty[0]
    else:
        return first_empty[0]
reserved_p(0)
print(first_empty_block())
put_block(0, 'a'*64)
put_block(1, 'a'*64)
print(reserved_p(0))
#del_block(0)
print(reserved_p(0))
print(first_empty_block())