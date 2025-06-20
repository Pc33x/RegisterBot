from os import getenv

from mcrcon import MCRcon

RCON_PASSWORD = getenv("RCON_PASSWORD")
RCON_IP = getenv("RCON_IP")
RCON_PORT = int(getenv("RCON_PORT"))

def give_permissions(nickname: str) -> None:
    with MCRcon(RCON_IP, RCON_PASSWORD, RCON_PORT) as rcon:
        rcon.command(f"pex user {nickname} group set player")