import json

videoFile='youtube.txt'

def load_data():
    
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []

def save_data(videos):
    with open(videoFile, 'w') as file:
        json.dump(videos, file)

def list_videos(videos):
    if not videos:
        print("No videos found.")
    else:
        print("\n")
        print("*" * 70)
        for index , video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, Duration: {video['time']} ")
        print("\n")
        print("*" * 70)

def add_video(videos):
    name=input("Enter Video Name: ")
    time=input("Enter Video Length: ")
    videos.append({'name':name,'time':time})
    save_data(videos)

def update_video(videos):
    list_videos(videos)
    index=int(input("Enter the Video number to Update: "))
    if 1<=index<=len(videos):
        name= input("Enter the New Video Name: ")
        time= input("Enter the New Video Length: ")
        videos[index-1]={'name':name, 'time':time}
        save_data(videos)
    else:
        print("Invalid Index Selected")

def delete_video(videos):
    list_videos(videos)
    index= int(input("Enter the Video number to Delete: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("Invalid Index Selected")

def main():
    while True:
        videos = load_data()
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
                list_videos(videos)
            case '2':
                print("\nAdding a YouTube video...")
                add_video(videos)
            case '3':
                print("\nUpdating a YouTube video...")
                update_video(videos)
            case '4':
                print("\nDeleting a YouTube video...")
                delete_video(videos)
            case '5':
                print("\nExiting the YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")

if __name__=="__main__":
    main()