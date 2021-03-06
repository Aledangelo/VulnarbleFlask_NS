# pip3 install mysql-connector-python
import mysql.connector


# Sarebbe buono valutare di usare anche il timeout per le connessioni
class MySql():
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306) -> None:
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__database = database

    def connect(self) -> None:  # Sta roba poi va gestita meglio con le eccezioni
        self.__conn = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            port=self.__port,
            database=self.__database
        )

    # Metodo generico dato un parametro (e una tabella) ritorna l'intera riga (in un dizionario) ad esso associata
    def selectRowByParam(self, paramKey: str, paramValue: str, table: str) -> list:
        query = f"SELECT * FROM {table} WHERE  {paramKey} = '{paramValue}';"
        # print(query)
        c = self.__conn.cursor(prepared=True)
        c.execute(query)
        rows = c.fetchall()  # In realtà qui tornerà sempre e solo una riga
        result = []
        for r in rows:  # Questo for viene eseguito solo una volta su una sola riga
            result.append(dict(zip(c.column_names, r)))
            # print(result)
        return result

    def updateRowByParam(self, paramKey1: str, paramValue: str, table: str, paramKey2: str, Value: str):
        query = f"UPDATE {table} SET {paramKey1} = '{Value}' WHERE  {paramKey2} = '{paramValue}';"
        # print(query)
        c = self.__conn.cursor(prepared=True)
        c.execute(query)
        self.__conn.commit()  # aggiorno il db, vedere cosa ritorna commit per eventuali check

    def insertAccount(self, paramValue1: str, paramValue2: str, paramValue3: str,
                  paramValue4: str, paramValue5: str, paramValue6: str, paramValue7: str, paramValue8: str):
        #try:
        query = f"INSERT INTO greenaccount(nome,cognome,citta,email,pwd,cellulare,nascita,valid) VALUES " \
                f"('{paramValue1}','{paramValue2}','{paramValue3}','{paramValue4}','{paramValue5}','{paramValue6}','" \
                f"{paramValue7}','{paramValue8}');"
        # print(query)
        c = self.__conn.cursor(prepared=True)
        c.execute(query)
        self.__conn.commit()
          #  return True
       # except:
          #  return False

    def deleteSession(self, paramValue: str, table: str):
        query = f"UPDATE {table} SET sessione = null WHERE id = {paramValue}"
        c = self.__conn.cursor(prepared=True)
        c.execute(query)
        self.__conn.commit()

    def deleteRowByParam(self, paramKey: str, paramValue: str, table: str):
        query = f"DELETE FROM {table} WHERE {paramKey} = '{paramValue}';"
        # print(query)
        c = self.__conn.cursor(prepared=True)
        c.execute(query)
        self.__conn.commit() #aggiorno db

    def insertToken(self, paramValue1: str, paramValue2: str, paramValue3: str, table: str):
        query = f"INSERT INTO {table}(id,token,userType) VALUES ('{paramValue1}','{paramValue2}','{paramValue3}');"
        # print(query)
        c = self.__conn.cursor(prepared=True)
        c.execute(query)
        self.__conn.commit()


if __name__ == '__main__':
    host='database-1.cpmyqifdjztx.us-east-1.rds.amazonaws.com'
    user='admin'
    password='3dun9d840fwedec-ceosdcsi'
    port=3306
    database='green'

    table = 'session'  # Quando crei il DB sii coerende con queste colonne
    paramKey = 'token'
    paramValue = '12'

    db = MySql(host, user, password, database, port)
    db.connect()
    r = db.insertAccount('giovanni','esposito','virginia' ,'ciao@ciao.com', 'ciao', '1234567', '10/10/10', str(123456))

# db = MySql(host, user, password, port, database)
# db.connect()
# r = db.selectRowByParam(paramKey, paramValue, table)
# print(r)
