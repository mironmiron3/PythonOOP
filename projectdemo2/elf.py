from projectdemo2.hero import Hero

class Elf(Hero):
    def __init__(self, llevel, name):
        super().__init__(llevel, name)


elf = Elf("E", "4")
print(str(elf))
