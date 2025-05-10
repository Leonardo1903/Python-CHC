import sqlite3

connect = sqlite3.connect('youtube_manager.db')

cursor=connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute('SELECT * FROM videos')
    for row in cursor.fetchall():
        print(f"ID: {row[0]}, Name: {row[1]}, Duration: {row[2]}")

def add_video(name, time):
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    connect.commit()

def update_video(videoId, name, time):
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (name, time, videoId))
    connect.commit()

def delete_video(videoId):
    cursor.execute('DELETE FROM videos WHERE id = ?', (videoId,))
    connect.commit()


def main():
    while True:
        print("\nWelcome to the YouTube Manager!")
        print("1. List all YouTube Videos")
        print("2. Add a YouTube Video")
        print("3. Update a YouTube Video details")
        print("4. Delete a YouTube Video")
        print("5. Exit")
        choice=input("\nPlease select an option: ")
    
        match choice:
            case '1':
                print("\nListing all YouTube videos...")
                list_videos()
            case '2':
                print("\nAdding a YouTube video...")
                name=input("Enter Video Name: ")
                time=input("Enter Video Length: ")
                add_video(name, time)
            case '3':
                print("\nUpdating a YouTube video...")
                videoId=input("Enter the Video ID to Update: ")
                name=input("Enter the New Video Name: ")
                time=input("Enter the New Video Length: ")
                update_video(videoId,name, time)
            case '4':
                print("\nDeleting a YouTube video...")
                videoId=input("Enter the Video ID to Delete: ")
                delete_video(videoId)
            case '5':
                print("\nExiting the YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")
                
    connect.close()


if __name__ == '__main__':
    main()