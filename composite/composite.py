class Member:
    def info(self):
        raise NotImplementedError


class Child(Member):

    __name__ = "child"

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am {self.name}, a {self.__name__} member.")


class Adult(Member):
    __name__ = "adult"

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"I am {self.name}, an {self.__name__} member.")


class MemberDirectory(Member):

    __name__ = "Member Directory"

    def __init__(self):
        self.members = set()

    def addMember(self, member: Member):
        print(
            f"Add {member.__name__} member: {member.name} into {self.__name__}.")
        self.members.add(member)

    def removeMember(self, member: Member):
        print(
            f"Remove {member.__name__} member: {member.name} from {self.__name__}.")
        self.members.remove(member)

    def info(self):
        print("Show each member's info:")
        for member in self.members:
            member.info()


if __name__ == "__main__":
    alex = Child("alex")
    bob = Child("bob")

    directory = MemberDirectory()
    directory.addMember(alex)
    directory.addMember(bob)

    directory.info()

    mark = Adult("mark")
    john = Adult("john")

    directory.addMember(mark)
    directory.addMember(john)
    directory.removeMember(alex)

    directory.info()
