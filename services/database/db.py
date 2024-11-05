import sqlite3

conection_timeout : float = 10.0
class database:
    is_connected = False
    connection = None
    cursors = []
    def get_sqlc(self,name : str) -> str|None: ## sql commands
        try:
            with open('./sql_query_commands/{}.sql'.format(name),'r') as file:
                if file:
                    val = str(file.read())
                    file.close()
                    return val
        except Exception as Error:
            print(Error)
        finally:
            return None
        
    def connect(self) -> sqlite3.Connection:
        """Create a new connection and connects"""
        if not self.is_connected:
            connection = sqlite3.connect(database='database.db',timeout=conection_timeout)
            self.connection = connection
            self.is_connected = True
            return self.connection

    def disconnect(self) -> None:
        """If there is any available connection, the connection are closed and all cursors are closed."""
        if self.is_connected:
            self.closeCursor(self.cursors)
            self.connection.close()
            self.connection = None

    def closeCursor(self,cursor : sqlite3.Cursor|list) -> None: 
        """Close all available cursors"""
        if type(cursor) == list and len(cursor) > 1:
            self.closeCursor(cursor[:len(cursor)//2])
            self.closeCursor(cursor[len(cursor)//2:])
            return
        if type(cursor) == sqlite3.Cursor:
            cursor.close()

    def create_cursor(self) -> sqlite3.Cursor|None:
        if self.is_connected:
            connection = self.connection
            cursor = connection.cursor()
            self.cursors.append(cursor)
            return cursor
        else:
            return None

    def commit(self) -> None:
        """commit the changes in database"""
        if self.is_connected:
            self.connection.commit()

    def rollback(self) -> None:
        """rollback changes in database"""
        if self.is_connected:
            self.connection.rollback()

    def run_command(self,command,args : tuple):
        command = self.get_sqlc(command)
        self.connect()
        try:
            cursor = self.create_cursor()
            cursor.execute(command,args)
            self.commit()
        except Exception as err:
            print(err)
        finally:
            self.rollback()
        self.disconnect()

    def run_writen(self,command : str,args : tuple):
        self.connect()
        try:
            cursor = self.create_cursor()
            cursor.execute(command,args)
            self.commit()
        except Exception as err:
            print(err)
        finally:
            self.rollback()
        self.disconnect()    

    def __init__(self) -> None:
        command = self.get_sqlc('setup')
        self.connect()
        try:
            cursor = self.create_cursor()
            cursor.execute(command)
            self.commit()
        except Exception as err:
            print(err)
        finally:
            self.rollback()
        self.disconnect()
        pass