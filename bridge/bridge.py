class Education:
    def info(self):
        raise NotImplementedError


class University(Education):
    def __init__(self, seniorHigh):
        self.seniorHigh = seniorHigh

    def info(self):
        print(self.getDiploma(), self.seniorHigh.getDiploma())

    def getDiploma(self):
        raise NotImplementedError


class UniversityA(University):
    def getDiploma(self):
        return "University A"


class UniversityB(University):
    def getDiploma(self):
        return "University B"


class UniversityC(University):
    def getDiploma(self):
        return "University C"


class SeniorHigh:
    def getDiploma(self):
        raise NotImplementedError


class SeniorHighA(SeniorHigh):
    def getDiploma(self):
        return "Senior High A"


class SeniorHighB(SeniorHigh):
    def getDiploma(self):
        return "Senior High B"


class SeniorHighC(SeniorHigh):
    def getDiploma(self):
        return "Senior High C"


if __name__ == "__main__":
    education = UniversityA(SeniorHighB())
    education.info()
