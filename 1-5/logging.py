import os
import logging

def create_logger_with_os(log_file="my_log.log"):
    # 로그 파일 경로 생성
    log_path = os.path.join(os.getcwd(), log_file)

    # 로그 객체 생성
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)

    # 파일 핸들러 설정
    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)

    # 콘솔 핸들러 설정
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 로그 포매터 설정
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 핸들러를 로거에 추가
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# 사용 예제
logger = create_logger_with_os()
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
