class Model:
    def __init__(self, fit_method, predict_method):
        self.fit_method = fit_method
        self.predict_method = predict_method

    def fit(self):
        self.fit_method.fit()

    def predict(self):
        self.predict_method.predict()

    def save_model(self):
        print("Model has saved.")

    def load_model(self):
        print("Model has loaded.")

    def set_fit_method(self, fit_method):
        self.fit_method = fit_method

    def set_predict_method(self, predict_method):
        self.predict_method = predict_method


class FitMethod:
    def fit(self):
        raise NotImplementedError


class NaiveFit(FitMethod):
    def fit(self):
        print("Naive Fit")


class EfficientFit(FitMethod):
    def fit(self):
        print("Efficient Fit")


class ExpensiveFit(FitMethod):
    def fit(self):
        print("Expensive Fit")


class PredictMethod:
    def predict(self):
        raise NotImplementedError


class NaivePredict(PredictMethod):
    def predict(self):
        print("Naive Predict")


class FastPredict(PredictMethod):
    def predict(self):
        print("Fast Predict")


class SlowPredict(PredictMethod):
    def predict(self):
        print("Slow Predict")


class CustomModel(Model):
    def __init__(self, fit_method, predict_method):
        super(CustomModel, self).__init__(fit_method, predict_method)

    def summary(self):
        print("Model Summary")


if __name__ == "__main__":
    naive_fit = NaiveFit()
    efficient_fit = EfficientFit()
    expensive_fit = ExpensiveFit()

    naive_predict = NaivePredict()
    fast_predict = FastPredict()
    slow_predict = SlowPredict()

    custom_model = CustomModel(naive_fit, naive_predict)
    custom_model.fit()
    custom_model.predict()

    custom_model.set_fit_method(efficient_fit)
    custom_model.fit()
    custom_model.predict()

    custom_model.set_predict_method(fast_predict)
    custom_model.fit()
    custom_model.predict()

    custom_model.save_model()
