import oracledb
import json


def confbi():
        
    try:
        conn = oracledb.connect("RM95053/191296@//oracle.fiap.com.br:1521/orcl")
    except Exception as err:
        print("Error connecting to database", err)
    else:
        print(conn.version)
        try:
            cur = conn.cursor()
            cur.execute(" TRUNCATE TABLE WANTEDFBI")

            with open('datareadyfbi.json') as file:
                data = json.load(file)
            for item in data['wanted']:
                sql_insert = """ INSERT INTO WANTEDFBI VALUES(:name, :dateOfBirth, :nationalities, :crimes, :gender) """
                cur.execute(sql_insert, item)
            

        except Exception as err:
            print("Error inserting Data", err)
        else:
            print("Insertion Complete")
            conn.commit()

    finally:
        cur.close()
        conn.close()

