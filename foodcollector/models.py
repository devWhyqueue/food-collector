from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str


@dataclass(frozen=True)
class Thread:
    name: str
    password: str
