class AbstractFactory:

    def getFactory(self, factoryType):
        if factoryType == "FactoryA":
            return FactoryA()

        if factoryType == "FactoryB":
            return FactoryB()


class IFactory:
    def getProduct(self):
        raise NotImplementedError


class FactoryA(IFactory):
    def getProduct(self, productType):
        if productType == "OldProduct":
            return OldProduct()

        if productType == "NewProduct":
            return NewProduct()

        raise ValueError("Product Not Found")


class FactoryB(IFactory):
    def getProduct(self, productType):
        if productType == "BigProduct":
            return BigProduct()
        if productType == "SmallProduct":
            return SmallProduct()

        raise ValueError("Product Not Found")


class Product:
    def info(self):
        raise NotImplementedError


class OldProduct(Product):
    def info(self):
        print("Old Product")


class NewProduct(Product):
    def info(self):
        print("New Product")


class BigProduct(Product):
    def info(self):
        print("Big Product")


class SmallProduct(Product):
    def info(self):
        print("Small Product")


if __name__ == "__main__":
    abstractFactory = AbstractFactory()

    factoryType = "FactoryA"
    productType = "OldProduct"
    factory = abstractFactory.getFactory(factoryType)
    product = factory.getProduct(productType)
    product.info()

    factoryType = "FactoryB"
    productType = "BigProduct"
    factory = abstractFactory.getFactory(factoryType)
    product = factory.getProduct(productType)
    product.info()
