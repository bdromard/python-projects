from hashlib import sha256

h = sha256()
h.update(b'python1990K00L')
hash = h.hexdigest()
print(hash)