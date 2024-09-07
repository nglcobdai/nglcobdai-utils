from nglcobdai_utils import Logger


def test_logger():
    logger = Logger("test_logger").logger
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    assert True
