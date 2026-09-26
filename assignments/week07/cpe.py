class pub_mod:

    def __intit__(self, name, age):
        self.name = name;
        self.age = age;

def Age(self):
    print("Age: ", self.age)

obj1 = pub_mod("Jason", 35);
print("Name: ", obj1.name)

obj2 = pub_mod("Nina", 16);
print("Name: ", obj2.name)


obj1.Age()
obj2.Age()