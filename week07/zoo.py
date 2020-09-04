from abc import ABCMeta, abstractmethod


class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            setattr(self, animal.__class__.__name__, True)
            self.animals.append(animal)
        else:
            raise Exception("duplicated animal")


class Animal(metaclass=ABCMeta):
    # def __init__(self):
    #     raise Exception("Animal cls cant be initialized")

    kind = None  # 类型
    size = None  # 体型
    character = None  # 性格
    ferocity = None  # 凶猛动物

    @abstractmethod
    def is_ferocious(self):
        size_dict = {"大": 3, "中等": 2, "小": 1}
        if self.kind == "食肉" and size_dict[self.size] >= 2 and self.character == "凶猛":
            return True
        return False


class Cat(Animal):
    def __init__(self, name, kind, size, character):
        self.name = name
        self.kind = kind
        self.size = size
        self.character = character

    voice = "miaomiaomiao"

    @property
    def is_pet(self):
        return not self.is_ferocious

    @property
    def is_ferocious(self):
        size_dict = {"大": 3, "中等": 2, "小": 1}
        if self.kind == "食肉" and size_dict[self.size] >= 2 and self.character == "凶猛":
            return True
        return False


class Dog(Animal):
    def __init__(self, name, kind, size, character):
        self.name = name
        self.kind = kind
        self.size = size
        self.character = character

    voice = "wangwangwang"

    @property
    def is_pet(self):
        return not self.is_ferocious

    @property
    def is_ferocious(self):
        size_dict = {"大": 3, "中等": 2, "小": 1}
        if self.kind == "食肉" and size_dict[self.size] >= 2 and self.character == "凶猛":
            return True
        return False


# 开始测试
if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    dog1 = Dog('大花狗 1', '食肉', '大', '凶猛')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    have_dog = hasattr(z, 'Dog')
    print(f"有猫吗？{have_cat}")
    print(f"有狗吗？{have_dog}")
    print(f"猫是宠物吗？{cat1.is_pet}")
    print(f"狗凶猛吗？{dog1.is_ferocious}")
    # a = Animal()  # Exception raised
