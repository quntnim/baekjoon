import hashlib
s = input()
st = s.encode('utf-8')
sha = hashlib.new('sha1')
sha.update(st)
print(sha.hexdigest())