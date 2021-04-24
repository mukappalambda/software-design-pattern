class IAlgorithm():
    def fit(self):
        raise NotImplementedError

    def save_model(self):
        raise NotImplementedError

    def load_model(self):
        raise NotImplementedError

    def predict(self):
        raise NotImplementedError


class AlgorithmFactory:
    def get_algorithm(self, alg_type):
        if alg_type == "naiveAlg":
            return naiveAlg()

        if alg_type == "goodAlg":
            return goodAlg()

        raise AssertionError("Algorithm Not Found")


class naiveAlg(IAlgorithm):

    def fit(self):
        print("naive Algorithm fit")

    def save_model(self):
        print("save naive model.")

    def load_model(self):
        print("load naive model.")

    def predict(self):
        print("naive Algorithm predict")


class goodAlg(IAlgorithm):

    def fit(self):
        print("good Algorithm fit")

    def save_model(self):
        print("save good model.")

    def load_model(self):
        print("load good model.")

    def predict(self):
        print("good Algorithm predict")


if __name__ == "__main__":
    alg_type = "goodAlg"
    algorithm_factory = AlgorithmFactory()
    alg = algorithm_factory.get_algorithm(alg_type=alg_type)

    alg.fit()
    alg.save_model()
    alg.load_model()
    alg.predict()
