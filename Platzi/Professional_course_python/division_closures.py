def make_division_by(n: int):
    assert n!=0, "No se puede dividir por zero"
    def number_to_divide(x: int)-> float:
        return x/n
    return number_to_divide

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    
    division_by_5 = make_division_by(5)
    print(division_by_5(10))
    
    division_by_18 = make_division_by(18)
    print(division_by_18(54))
    
if __name__ == "__main__":
    run()
