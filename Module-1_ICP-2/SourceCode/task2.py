# 1st approach
def string_alternative(mystr):
    my_alterntative_str = ""
    for i in range(len(mystr)):
        if i % 2 == 0:
            my_alterntative_str += mystr[i]
    return my_alterntative_str


## 2nd approach
def string_alternative2(mystr):
    new_str = ""
    for j in range(0, len(mystr), 2):
        new_str += mystr[j]
    return new_str


if __name__ == "__main__":
    mystr = "Good evening"
    print(f"Input text: {mystr}")
    print(f"Output with first  approach: {string_alternative(mystr)}")
    print(f"Output with second approach: {string_alternative2(mystr)}")
