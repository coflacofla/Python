import logging
logging.basicConfig(filename='my__log.log',encoding='utf-8',level=logging.DEBUG)
logging.debug('This is message should go to the loge file')
logging.info('So should this')
logging.warning('And this,too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')


