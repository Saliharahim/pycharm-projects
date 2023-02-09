name="moothedam"
def programming():
    def python():
        global  name
        name="saliha"

    def mearn():
        nonlocal name  #access outer the function
        name="duaa"

    def flutter():
        #global name
        name="sajna"

    name="sainaba"

    python()
    mearn()
    print("coder is:",name)

programming()
print(name)