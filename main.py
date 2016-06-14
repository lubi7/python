import pymysql
import pymysql.cursors

def main():
    try:
        conn = pymysql.connect(host='db4free.net', port=3306, user='lubii', passwd='zaq1@WSX', db='python_db')
        cur = conn.cursor();
        cur.execute("select * from user")

        for row in cur:
            print(row)
    except:
        print("Opss... problem with connection")


if __name__ == "__main__":
    main()
