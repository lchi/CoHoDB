import sqlite3 as lite

dbName = 'coho.db'

class CoHoData:

    def __init__(self, dbName='coho.db'):
        try:
            db = lite.connect(dbName)    
            self.db = db
        except lite.Error, e:
            raise IOError("Error: cannot connect to %s" % dbName)
    
    def __del__(self):            
        if self.db:
            self.db.close()

    #Note - this method of insertion is very insecure
    #beware or special characters (esp parens)
    def add_record(self, group_id='NULL', 
                   strategy='NULL',
                   trade_date='NULL',
                   expiration_date='NULL',
                   underlyer='NULL',
                   type='NULL',
                   position='NULL',
                   strike='NULL',
                   spot='NULL',
                   premium='NULL',
                   quantity='NULL',
                   commission='NULL',
                   industry='NULL',
                   trade_type='NULL',
                   asset_type='NULL',
                   notes='NULL'):
        statement = """insert into trade_records values(NULL, """ + str(group_id) + """, 
'""" + strategy+ """', '""" + trade_date+ """', '""" + expiration_date+ """', '""" + underlyer+ """', '""" + type+ """', '""" + position+ """', '""" + str(strike) + """', '""" + str(spot) + """', '""" + str(premium) + """', '""" + str(quantity)+ """', '""" + str(commission)+ """', '""" + industry+ """', '""" + trade_type+ """', '""" + asset_type+ """', '""" + notes+ """');
"""
        cursor = self.db.cursor()
        cursor.execute(statement)
        self.db.commit()

    def get_schema(self):
        c = self.db.cursor()
        c.execute("pragma table_info(trade_records);")
        print  c.fetchall()
        
def main():
    data = CoHoData()
    data.add_record(**{'underlyer':'goog', 'type':'put', 'quantity':300})
    data.get_schema()

if __name__ == "__main__":
    main()
