# error-log file

import logging
from datetime import datetime

class Data_Logger:
    """
    Data Logger class

    Attributes:
        __log_file_name: log file name, 데이터 로그 파일 이름
        __logger_level: log level, 로그 레벨
        __logger: logger object, 로거 객체
    
    Methods:
        set_logger: set logger level, 로거 레벨 설정
        get_logger_level: get logger level, 로거 레벨 반환
        text_loging: write log to log file, 로그 파일에 로그 기록
    """
    def __init__(self, log_level="INFO", log_msg=""):
        self.__INFO_log_file_name = "info_log.txt"
        self.__ERROR_log_file_name = "error_log.txt"
        self.__DEBUG_file_name = "debug_log.txt"
        self.__WARNING_file_name = "warning_log.txt"
        self.__sys_log_file_name = "sys_log.txt"
        self.__log_msg = log_msg
        self.__logger_level = log_level
        self.__logger = logging.getLogger(log_level)

    def __str__(self):
        return f"Data_Logger({self.__log_file_name}, {self.__logger_level})" 
    
    def set_logger(self, log_level):
        """
        Set Logger Level Method
        로거 레벨을 설정하는 메소드
        """
        self.__logger.setLevel(log_level)
    
    def get_logger_level(self):
        """
        Get Logger Level Method
        로거 레벨을 반환하는 메소드
        """
        return self.__logger_level
    
    def log_msg_process(self, log_msg):
        """
        Log Message Process Method
        입력받은 로그 메시지를 로그 파일에 기록하는 메소드
        """
        if self.__logger_level == "INFO":
            self.__logger.info(log_msg)
            INFO_log_file = open(self.__INFO_log_file_name, 'a')
            INFO_log_file.write(log_msg)
        elif self.__logger_level == "ERROR":
            self.__logger.error(log_msg)
            error_log_file = open(self.__ERROR_log_file_name, 'a')
            error_log_file.write(log_msg)
        elif self.__logger_level == "DEBUG":
            self.__logger.debug(log_msg)
            debug_log_file = open(self.__DEBUG_file_name, 'a')
            debug_log_file.write(log_msg)
        elif self.__logger_level == "WARNING":
            self.__logger.warning(log_msg)
            warning_log_file = open(self.__WARNING_file_name, 'a')
            warning_log_file.write(log_msg)

    def text_loging(self):
        """
        Text Loging Method
        Sys 로그 파일에 있는 로그를 구별하여 기록하는 메소드
        """
        sys_log_file = open(self.__sys_log_file_name, 'r')
        for line in sys_log_file:
            if "INFO" in line:
                INFO_log_file = open(self.__INFO_log_file_name, 'a')
                INFO_log_file.write(line)
                INFO_log_file.close()

            if "ERROR" in line:
                error_log_file = open(self.__ERROR_log_file_name, 'a')
                error_log_file.write(line)
                error_log_file.close()

            if "DEBUG" in line:
                debug_log_file = open(self.__DEBUG_file_name, 'a')
                debug_log_file.write(line)
                debug_log_file.close()
            
            if "WARNING" in line:
                warning_log_file = open(self.__WARNING_file_name, 'a')
                warning_log_file.write(line)
                warning_log_file.close()


Data_Logger = Data_Logger('error_log.txt')
print(Data_Logger.get_logger_level())
Data_Logger.text_loging("test")
