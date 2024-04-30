class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            return self.successor.handle_request(request)
        else:
            print("End of chain reached, request not handled.")


class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == "A":
            print("ConcreteHandlerA handles request 'A'.")
        else:
            super().handle_request(request)


class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == "B":
            print("ConcreteHandlerB handles request 'B'.")
        else:
            super().handle_request(request)


class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == "C":
            print("ConcreteHandlerC handles request 'C'.")
        else:
            super().handle_request(request)


# Usage
handler_c = ConcreteHandlerC()
handler_b = ConcreteHandlerB(successor=handler_c)
handler_a = ConcreteHandlerA(successor=handler_b)

# Start the chain by passing a request to the first handler
handler_a.handle_request("A")  # Output: ConcreteHandlerA handles request 'A'.
handler_a.handle_request("B")  # Output: ConcreteHandlerB handles request 'B'.
handler_a.handle_request("C")  # Output: ConcreteHandlerC handles request 'C'.
handler_a.handle_request("D")  # Output: End of chain reached, request not handled.
