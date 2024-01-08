import logging

def test_print_logs():
    LOGGER = logging.getLogger(__name__)

    LOGGER.info("This is information Log")
    LOGGER.warning("This is warning Log")
    LOGGER.error("This is error Log")
    LOGGER.critical("This is critical Log")
