import sqlite3

conn = sqlite3.connect('youtube_manager.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    for video in videos:
        print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name,time) Values (?,?)",(name,time))
    conn.commit()
    
def update_video(new_name,time,id):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?",(new_name,time,id))
    conn.commit() 

def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id=?", (id,))
    conn.commit()


def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name,time)
        elif choice == "3":
            id = input("Enter video ID to Update: ")
            new_name = input("Enter the new video name: ")
            time = input("Enter the new video time: ")
            update_video(new_name,time,id)
        elif choice == "4":
            id = input("Enter video ID to Delete: ")
            delete_video(id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    conn.close()

if __name__ == "__main__":
    main()