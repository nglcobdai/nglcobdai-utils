import os
from pathlib import Path

import yaml
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(
        env_file=(
            ".env" if os.getenv("ENV", None) is None else f".env.{os.getenv('ENV')}"
        ),
        env_file_encoding="utf-8",
        extra="allow",
        case_sensitive=True,
    )

    def set_yaml(self, path):
        """Set settings from yaml file

        Args:
            path (str or Path): Path of the yaml file
        """
        data = self.load_yaml(path)

        for key, value in data.items():
            setattr(self, key, value)

    @staticmethod
    def load_yaml(path):
        """Load yaml file

        Args:
            path (Path): Path of the yaml file

        Returns:
            Dict[*]: Data of the yaml file
        """
        path = path if isinstance(path, Path) else Path(path)

        if not path.exists():
            raise FileNotFoundError(f"{path} not found")

        with open(path, "r") as f:
            file = f.read()
            return yaml.safe_load(file)
