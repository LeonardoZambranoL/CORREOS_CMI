import pymysql



class DataBase:
    
        
    def __init__(self,i):
        self.connection = pymysql.connect(
            host=i[4],
            user=i[5],
            passwd=i[6],
            db=i[7],
            autocommit=True
        )

        self.cursor = self.connection.cursor()

        #print ("Se establecio la conexion a la base de datos")

    def get_mail(self,i,COLUMN,COND,limite):
        #sql ="SELECT CORREO FROM destinatario WHERE ENVIO = {}".format(COND)
        TABLE=i[8]
        sql ="SELECT * FROM `{}` WHERE `{}` {} limit {}".format(TABLE,COLUMN,COND,limite)
        #print(sql)
        #print("SELECT")
        try:
            self.cursor.execute(sql)
            correos=self.cursor.fetchall()

            #print (correos)
            correos=[a for a in correos]
            return correos
            
        except Exception as e:
            return "Error al Buscar en la base de datos: "+str(e)
        

    def update_status(self,i,COLUMN,STATUS,CODIGO):
        TABLE=i[8]
        sql ="UPDATE `{}` SET `{}`={} WHERE CODIGO={}".format(TABLE,COLUMN,STATUS,CODIGO)
        #print(sql)
        try:
            self.cursor.execute(sql)
            return "Base de datos Actualizada"
            
        except Exception as e:
            return "Error al Actualizar la base de datos :"+str(e)

    def count(self,i,COLUMN,COND):
        TABLE=i[8]
        sql ="SELECT COUNT(*) FROM `{}` WHERE `{}` {}".format(TABLE,COLUMN, COND)
        #print(sql)
        #print("SELECT")
        try:
            self.cursor.execute(sql)
            number=self.cursor.fetchall()

            #print (correos)

        
            return number[0][0]
            
        except Exception as e:
            return "Error al Buscar en la base de datos: "+str(e)
        
    def add_column(self,i,COLUMN):
        TABLE=i[8]
        sql ="ALTER TABLE `{}` ADD COLUMN `{}` VARCHAR(45) NULL".format(TABLE,COLUMN)
        #print(sql)
        #print("SELECT")
        try:
            self.cursor.execute(sql)
        

            
        except Exception as e:
            print(str(e))
                
        
    def Close(self):
        self.connection.close()


    
    
def update_status(i,Template,New_status,Code):
    try:
        database = DataBase(i)
        update=database.update_status(i,Template,"'"+New_status+"'","'"+Code+"'")
        database.Close()
        return update
    except:

        return "Error de Actualización:  Error al Conectar a la base de datos"
    
    
def general_fetch(i,Template,Cond,Limit):
    try:
        database = DataBase(i)
        correos=database.get_mail(i,Template,Cond,Limit)
        database.Close()
        return correos
    except:
        return "Error al Buscar en la base de datos:  Error al Conectar a la base de datos"

    
    

def fetch_new_mails(i,Template,Limit):
    return general_fetch(i,Template,"IS NULL OR '"+Template+"' IN ('',' ')",Limit)

def fetch_sent_mails(i,Template,Limit):
    return general_fetch(i,Template,"='ENVIADO'",Limit)
    
def fetch_error_mails(i,Template,Limit):
    return general_fetch(i,Template,"='ERROR'",Limit)
    

def fetch_other_mails(i,Template,Limit):
    return general_fetch(i,Template,"NOT in ('ERROR','ENVIADO') AND "+Template+" is NOT NULL",Limit)
    

def general_count(i,Template,Cond):
    try:
        database = DataBase(i)
        number=database.count(i,Template,Cond)
        database.Close()
        return number
    except:
        return "Error al Buscar en la base de datos:  Error al Conectar a la base de datos"

def count_new(i,Template):
    return general_count(i,Template,"IS NULL OR '"+Template+"' IN ('',' ')")

def count_sent(i,Template):
    return general_count(i,Template,"='ENVIADO'")


def add_column(i,Template):
    try:
        database = DataBase(i)
        database.add_column(i,Template)
        database.Close()
        
    except:
        pass

if __name__ == '__main__':
    pass

""" CÓDIGO DE PRUEBAS


    i=['XXXXXXXXX', 'XXXXXXXXX', 'XXXXXXXXXXXXXXXX', 'XXXXXXX', 'XXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXX', 'XXXXXXXXX']
    
    Template="NUEVO 4"
    add_column(i,Template)
    
    
        
    new_mails=fetch_new_mails(i,Template,5)
    sent_mails=fetch_sent_mails(i,Template,5)
    
    ammount_new=count_new(i,Template)
    ammount_sent=count_sent(i,Template)
    
    
    
    print("NUEVOS : ",[a[0] for a in new_mails], "TOTAL : ", ammount_new)
    print("ENVIADOS : ",[a[0] for a in sent_mails], "TOTAL : ", ammount_sent)
        

    Db="CMI"
    Table="ensayo"
    Template="ZOOM"
    new_mails=fetch_new_mails(i,Db,Table,Template,5)
    sent_mails=fetch_sent_mails(i,Db,Table,Template,5)
    error_mails=fetch_error_mails(i,Db,Table,Template,5)
    other_mails=fetch_other_mails(i,Db,Table,Template,5)
    
    print("NUEVOS : ",new_mails)
    print("ENVIADOS : ",sent_mails)
    print("ERROR : ",error_mails)
    print("OTROS : ",other_mails)
    #print(MySQL_for_massive_mails.update_status(Db,Table,Template_name,"ERROR",new_mails[0][0]),"|  ERROR  |",new_mails[0][0],"\n")
    print(update_status(i,Db,Table,Template,"ERROR","HVY006"))

    
        

"""