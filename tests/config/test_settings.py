from nglcobdai_utils import Settings


def test_settings():
    settings = Settings()
    assert settings.PROJECT_NAME == "nglcobdai-utils"
