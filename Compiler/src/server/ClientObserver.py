# @Author Jose Daniel Acuna
# Last time edited 11/1/19


class ClientObserver:

    observers = []
    client_response = ""

    @staticmethod
    def update(message):
        for observer in ClientObserver.observers:
            observer.update(message)
