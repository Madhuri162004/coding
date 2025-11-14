class dog:
    speak="bark"
    breed="golden retriever"
    def about(self):
        return f"i am a dog, i can {self.speak} and my bread is {self.breed}"
d1=dog()
print(d1.speak)
print(d1.breed)
print(d1.about())
class cat:
    speak="meow"
    breed="persian"
    def about(self):
        return f"i am a cat, i can {self.speak} and my bread is {self.breed}"
c1=cat()
print(c1.speak)
print(c1.breed)
print(c1.about())
class person:
    name="john"
    age=25
    def info(self):
        return f"my name is {self.name} and my age is {self.age}"
p1=person()
print(p1.name)
print(p1.age)
print(p1.info())