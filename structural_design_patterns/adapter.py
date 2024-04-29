# Existing logging library (OldLogger)
class OldLogger:
    def log(self, message):
        print(f"[OldLogger] Logging message: {message}")


# New logging library (NewLogger)
class NewLogger:
    def log_message(self, msg):
        print(f"[NewLogger] Logging message: {msg}")


# Adapter to adapt NewLogger to the interface of OldLogger
class NewToOldLoggerAdapter(OldLogger):
    def __init__(self, new_logger):
        self.new_logger = new_logger

    def log(self, message):
        # Adapt the interface of NewLogger to match the OldLogger interface
        self.new_logger.log_message(message)


# Example usage
# Instantiate the new logger
new_logger = NewLogger()

# Create an adapter instance passing the new logger
adapter = NewToOldLoggerAdapter(new_logger)

# Use the adapter to log messages, just like the old logger
adapter.log("This is a message logged using the new logger via adapter")
