
from pytapo import Tapo
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

if __name__ == '__main__':

