class IObservable:
    def subscribe(self, observer):
        raise NotImplementedError

    def unsubscribe(self, observer):
        raise NotImplementedError

    def notify(self):
        raise NotImplementedError


class Subject(IObservable):
    def __init__(self, name):
        self.name = name
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer.notify(*args, **kwargs)


class IObserver:
    def notify(self):
        raise NotImplementedError


class Observer(IObserver):
    def __init__(self, name):
        self.name = name

    def notify(self, title, body):
        print(f"{self.name} Got New Challenge! Title: {title} and Body: {body}")


if __name__ == "__main__":
    workout = Subject("workout")
    alex = Observer("alex")
    bob = Observer("bob")
    mark = Observer("mark")

    workout.subscribe(alex)
    workout.subscribe(bob)

    first_content = {
        "title": "Burpee Workout",
        "body": "Go Hard or Go Harder"
    }

    workout.notify(**first_content)

    second_content = {
        "title": "Chest Workout Routine",
        "body": "No Pain No Gain"
    }

    workout.subscribe(mark)
    workout.notify(**second_content)

    third_content = {
        "title": "Street Workout",
        "body": "Pull Up or Shut Up"
    }

    workout.unsubscribe(bob)
    workout.notify(**third_content)
