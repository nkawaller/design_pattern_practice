class Component:
    def operation(self) -> str:
        pass

class ConcreteComponent(Component):
    def operation(self) -> str:
        return "This is the concrete component"

class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component
    def operation(self) -> str:
        return self._component.operation()

class ConcreteDecoratorOne(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorOne({self.component.operation()})"

class ConcreteDecoratorTwo(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorTwo({self.component.operation()})"

def client_code(component: Component) -> None:
    print(f"RESULT: {component.operation()}", end='')