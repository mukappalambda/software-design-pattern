class Builder:

    def getTable(self):
        raise NotImplementedError

    def getChair(self):
        raise NotADirectoryError

    def getBed(self):
        raise NotImplementedError


class GoodRoomBuilder(Builder):
    def __init__(self):
        self.table = "Good Table"
        self.chair = "Good Chair"
        self.bed = "Good Bed"

    def getTable(self) -> str:
        return self.table

    def getChair(self) -> str:
        return self.chair

    def getBed(self) -> str:
        return self.bed


class Room:

    def setTable(self, table: str):
        self.table = table

    def setChair(self, chair: str):
        self.chair = chair

    def setBed(self, bed: str):
        self.bed = bed

    def info(self):
        info = dict(table=self.table, chair=self.chair, bed=self.bed)
        print(info)


class Director:
    def setBuilder(self, builder: Builder):
        self.table = builder.getTable()
        self.chair = builder.getChair()
        self.bed = builder.getBed()

    def getRoom(self) -> Room:
        room = Room()
        room.setTable(self.table)
        room.setChair(self.chair)
        room.setBed(self.bed)
        return room


if __name__ == "__main__":
    goodRoomBuilder = GoodRoomBuilder()

    director = Director()
    director.setBuilder(goodRoomBuilder)
    room = director.getRoom()
    room.info()
