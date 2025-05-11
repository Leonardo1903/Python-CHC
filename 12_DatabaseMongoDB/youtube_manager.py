from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db=client["YoutubeManager"]
videos_collection = db["videos"]

def list_videos():
    for video in videos_collection.find():
        print(f"Video ID: {video['_id']}, Name: {video['name']}, Length: {video['time']}")

def add_video(name, time):
    videos_collection.insert_one({"name": name, "time": time})

def update_video(videoId, name, time):
    videos_collection.update_one(
        {"_id": ObjectId(videoId)},
        {"$set": {"name": name, "time": time}}
        )

def delete_video(videoId):
    videos_collection.delete_one({"_id":ObjectId( videoId)})

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
                
    

if __name__ == "__main__":
    main()