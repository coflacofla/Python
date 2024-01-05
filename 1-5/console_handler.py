import logging as l

# 로그 설정
l.basicConfig(level=logging.INFO)

# 로그 생성
logger = l.getLogger("console_logger")

# 콘솔 핸들러 생성
console_handler = l.StreamHandler()

# 콘솔 핸들러를 로거에 추가
logger.addHandler(console_handler)

# 로그 메시지 작성
l.info("This is an info message.")
l.warning("This is a warning message.")
