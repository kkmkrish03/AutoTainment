import argparse
import logging

def setup_logging(enable_logging):
    log_level = logging.DEBUG if enable_logging else logging.ERROR
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

def main(enable_logging):
    # Your main script logic goes here
    logging.debug("This is a debug message")
    logging.info("This is an info message")
    logging.warning("This is a warning message")
    logging.error("This is an error message")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script with logging on/off argument")
    parser.add_argument("--enable-logging", action="store_true", help="Enable logging")
    args = parser.parse_args()

    setup_logging(args.enable_logging)
    main(args.enable_logging)
