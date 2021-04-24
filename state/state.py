class WeatherState:
    def response(self):
        raise NotImplementedError


class WeatherStateContext:
    def __init__(self):
        self.current_state = Sunny()

    def set_state(self, state):
        self.current_state = state

    def response(self):
        self.current_state.response(self)


class Sunny(WeatherState):
    def __init__(self):
        self.name = "sunny"

    def response(self, ctx: WeatherStateContext):
        print(f"The weather is {self.name} now. Go hiking!")


class Cloudy(WeatherState):
    def __init__(self):
        self.name = "cloudy"

    def response(self, ctx: WeatherStateContext):
        print(f"The weather is {self.name} now. Climbing!")


class Rainy(WeatherState):
    def __init__(self):
        self.name = "rainy"

    def response(self, ctx: WeatherStateContext):
        print(f"The weather is {self.name} now. Reading at home!")


if __name__ == "__main__":
    state_context = WeatherStateContext()
    state_context.response()

    state_context.set_state(Cloudy())
    state_context.response()

    state_context.set_state(Rainy())
    state_context.response()
