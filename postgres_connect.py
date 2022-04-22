import psycopg2

def runquery(sql):
    try:
        connection=psycopg2.connect(user="ofbqtxxmxboxbm",password="b599b5cc38b5878b8ed21e41e1c4174c25c756ef8a404dd6da5c8dfa4815be84",host="ec2-52-203-118-49.compute-1.amazonaws.com",database="dcsudgtuo5s500")
        cursor=connection.cursor()
        cursor.execute(sql)
        record=cursor.fetchall()
        return record
    except:
        print("errror whlie fetching data")
    finally:
        cursor.close()
        connection.close()
