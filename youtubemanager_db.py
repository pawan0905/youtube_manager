import sqlite3
conn=sqlite3.connect('yotubemng.db')
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows=cursor.fetchall()
    if not rows:
        print("no videos found")
        exit()
    else:
        for row in rows:
           print(row)
def add_videos(name,time):
    cursor.execute("INSERT INTO videos(name,time) VALUES(?,?)",(name,time))
    conn.commit()


def  update_videos(video_id,name,time):
     cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(name,time,video_id))
     conn.commit()
def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    conn.commit()
def main():
    while True:
        print("\n Youtube Manager App With DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit program")
        choice=input("Enter Your Choice : ")
        if choice=="1":
            list_videos()
        elif choice=="2":
            name=input("Enter your Video Name : ")
            time=input("Enter video time : ")
            add_videos(name, time)
        elif choice=="3":
            video_id=input("Enter video id : ")
            name=input("Enter video name : ")
            time=input("Enter video time : ")
            update_videos(video_id,name,time)
        elif choice == "4":
            video_id=input("Enter video id : ")
            delete_videos(video_id)
        elif choice=="5":
            break
        else:
            print("invalid choice")
    conn.close()
if __name__=="__main__":
    main()