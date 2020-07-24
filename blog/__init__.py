
# 进行转换, 让pymysql的内容转换为mysqldb,以便于ORM能够匹配
from pymysql import install_as_MySQLdb

install_as_MySQLdb()