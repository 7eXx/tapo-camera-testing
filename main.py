
from pytapo import Tapo
from dotenv import dotenv_values

config = {
    **dotenv_values(".env"),
    **dotenv_values(".env.local")
}

tapo = Tapo(config["TAPO_IP"], config["TAPO_USERNAME"], config["TAPO_PASSWORD"])



def set_home_mode() -> None:
    tapo.setMotionDetection(False)
    tapo.setPersonDetection(False)
    tapo.setTamperDetection(False)
    tapo.setAlarm(False)
    tapo.setNotificationsEnabled(False)
    tapo.setPrivacyMode(True)

def set_away_mode() -> None:
    tapo.setMotionDetection(True)
    tapo.setPersonDetection(True)
    tapo.setTamperDetection(True)
    tapo.setAlarm(True)
    tapo.setNotificationsEnabled(True)
    tapo.setPrivacyMode(False)

if __name__ == '__main__':
    privacy_mode = tapo.getPrivacyMode()
    print(f"Privacy mode: {privacy_mode}")

    motion = tapo.getMotionDetection()
    print(f"Motion detection: {motion}")

    alarm = tapo.getAlarm()
    print(f"Alarm: {alarm}")

