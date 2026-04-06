import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_video(videos):
    for index, video in enumerate(videos, start=1):
        print(f"{index}. Title: {video['title']}, URL: {video['url']}")

def add_video(videos):
    title = input("Enter video name: ")
    url = input("Enter video url/time: ")
    videos.append({"title": title, "url": url})
    helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the number of the video to update: "))
    if 1 <= index <= len(videos):
        title = input("Enter new video name: ")
        url = input("Enter new video url/time: ")
        videos[index - 1] = {"title": title, "url": url}
        helper(videos)
    else:
        print("Invalid index. Please try again.")

def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the number of the video to delete: "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        helper(videos)
    else:        
        print("Invalid index. Please try again.")

def main():
    videos = load_data()

    while True:
        print("\nYoutube Manager")
        print("1. Add a video")
        print("2. List all videos")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("Adding a video...")
                add_video(videos)

            case "2":
                print("Listing all videos...")
                list_all_video(videos)

            case "3":
                print("Updating a video...")
                update_video(videos)

            case "4":
                print("Deleting a video...")
                delete_video(videos)

            case "5":
                print("Exiting...")
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()