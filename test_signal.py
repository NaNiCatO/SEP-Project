from PySide6.QtCore import QObject, Signal

class Emitter(QObject):
    # Create a custom signal named hello_signal
    hello_signal = Signal(str)
    


    def emit_hello(self):
        # Emit the hello_signal with the message "Hello world!"
        self.hello_signal.emit("Hello world!")

class Receiver(QObject):
    # Define a slot function decorated with @Slot
    def handle_hello(self, message):
        # Print the received message
        print(message)

if __name__ == "__main__":
    # Create an instance of the Emitter class
    emitter = Emitter()

    # Create an instance of the Receiver class
    receiver = Receiver()

    # Connect the hello_signal of the emitter to the handle_hello slot of the receiver
    emitter.hello_signal.connect(receiver.handle_hello)

    # Call the emit_hello method to trigger the signal emission
    emitter.emit_hello()
