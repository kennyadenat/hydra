# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from omegaconf import DictConfig

import hydra


class DBConnection:
    def connect(self) -> None:
        pass


class MySQLConnection(DBConnection):
    def __init__(self, host: str, user: str, password: str) -> None:
        self.host = host
        self.user = user
        self.password = password

    def connect(self) -> None:
        print(
            f"MySQL connecting to {self.host} with user={self.user} and password={self.password}"
        )


class PostgreSQLConnection(DBConnection):
    def __init__(self, host: str, user: str, password: str, database: str) -> None:
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self) -> None:
        print(
            f"PostgreSQL connecting to {self.host} with user={self.user} "
            f"and password={self.password} and database={self.database}"
        )


@hydra.main(config_path="conf/config.yaml")
def my_app(cfg: DictConfig) -> None:
    connection = hydra.utils.instantiate(cfg.db)
    connection.connect()


if __name__ == "__main__":
    my_app()
