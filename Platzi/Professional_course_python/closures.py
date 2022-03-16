def make_repeat_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes usar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeat_of(5)
    repeat_10 = make_repeat_of(10)
    print(repeat_5("hi"))
    print(repeat_10("Xd "))
    
    
if __name__ == "__main__":
    run()
