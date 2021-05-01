class Builder:
    def buildTable(self):
        raise NotImplementedError

    def buildChair(self):
        raise NotADirectoryError

    def buildBed(self):
        raise NotImplementedError

    def getResult(self):
        raise NotImplementedError


class GoodRoomBuilder(Builder):
    __name__ = "Good Room Builder"

    def buildTable(self) -> None:
        self.table = "Good Table"
        return

    def buildChair(self) -> None:
        self.chair = "Good Chair"
        return

    def buildBed(self) -> None:
        self.bed = "Good Bed"
        return

    def getResult(self) -> None:
        print(f"{self.table}; {self.chair}; {self.bed}")


class Director:
    def __init__(self, builder: Builder):
        self.builder = builder
        print(f"Instantiate director with {self.builder.__name__}")

    def build(self):
        print(f"Invoke build method...")
        self.builder.buildTable()
        self.builder.buildChair()
        self.builder.buildBed()


if __name__ == "__main__":
    goodRoomBuilder = GoodRoomBuilder()

    director = Director(builder=goodRoomBuilder)
    director.build()
    goodRoomBuilder.getResult()
