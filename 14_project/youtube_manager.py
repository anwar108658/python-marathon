import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        return json.dump(videos,file)

def list_all_video(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index} {video}")

def add_video(videos):
    name = input("Enter video name : ")
    time = input("Enter video time : ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter video name : ")
        time = input("Enter video time : ")
        videos[index - 1] = {'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid index")
    

def delete_video(videos):
    list_all_video(videos)
    index = int(input("Enter the video number to delete"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_data_helper(videos)
    else:
        print("invalid index")
        

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Chose  an option")
        print("\n 1. List all youtube videos")
        print("\n 2. Add a youtube")
        print("\n 3. Update a youtube video details")
        print("\n 4. Delete a youtube video")
        print("\n 4. Exit the app")
        choice = input("Enter your choice : ")
        print(videos)
        
        match choice:
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
                
                
if __name__ == "__main__": 
    main()