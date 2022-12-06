from hashlib import md5

### PART 1
# m = md5()
# out = 0
# digest = "fffffffffffffffff"
# while digest[:5] != "00000":
#     out += 1
#     digest = md5(f"bgvyzdsv{out}".encode()).hexdigest()

# print(digest)
# print(out)

### PART 2
m = md5()
out = 0
digest = "fffffffffffffffff"
while digest[:6] != "000000":
    out += 1
    digest = md5(f"bgvyzdsv{out}".encode()).hexdigest()

print(out)
