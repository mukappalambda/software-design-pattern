class RoomElement:
    def accept(self, visitor):
        raise NotImplementedError


class Door(RoomElement):
    def accept(self, visitor):
        visitor.visitDoor(self)


class Furniture(RoomElement):
    def accept(self, visitor):
        visitor.visitFurniture(self)


class Bed(RoomElement):
    def accept(self, visitor):
        visitor.visitBed(self)


class RoomElementVisitor:
    def visitDoor(self, element):
        raise NotImplementedError

    def visitFurniture(self, element):
        raise NotImplementedError

    def visitBed(self, element):
        raise NotImplementedError


class RoomElementFriendVisitor(RoomElementVisitor):
    def visitDoor(self, door):
        print("Friend visiting door")

    def visitFurniture(self, furniture):
        print("Friend visiting furniture")

    def visitBed(self, bed):
        print("Friend visiting bed")


class RoomElementParentsVisitor(RoomElementVisitor):
    def visitDoor(self, door):
        print("Parents visiting door")

    def visitFurniture(self, furniture):
        print("Parents visiting furniture")

    def visitBed(self, bed):
        print("Parents visiting bed")


class Room(RoomElement):
    def __init__(self):
        self.elements = [Door(), Furniture(), Bed()]

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)


if __name__ == "__main__":
    room = Room()
    room.accept(RoomElementFriendVisitor())
    room.accept(RoomElementParentsVisitor())
