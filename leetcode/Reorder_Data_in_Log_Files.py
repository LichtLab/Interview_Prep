

class reversor:
    def __init__(self, obj):
        self.obj = obj

    def __eq__(self, other):
        return other.obj == self.obj

    def __lt__(self, other):
        return other.obj < self.obj


let_list = ["a8 act zoo", "g1 act car", "a2 act car", "ab1 off key dog"]
ext_let_list = []
for elm in let_list:
    idnt = elm.split(' ')[0]
    cntnt = " ".join(elm.split(' ')[1:])
    ext_let_list.append([idnt, cntnt])

print(ext_let_list)
ext_let_list = sorted(
    ext_let_list,
    key=lambda y: (
        y[1],
        reversor(y[0]))
    )
print(ext_let_list)
