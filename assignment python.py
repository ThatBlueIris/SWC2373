import requests

class WebexTroubleshootingTool:
    def __init__(self):
        self.base_url = "https://webexapis.com/v1"
        self.headers = {"Authorization": f"Bearer {input('Enter Webex Token: ')}"}

    def test_connection(self):
        try:
            response = requests.get(f"{self.base_url}/people/me", headers=self.headers)
            response.raise_for_status()
            print("Connection successful!")
        except requests.exceptions.HTTPError as err:
            print(f"Error: {err}")
        input("Press Enter to go back to the menu...")

    def display_user_info(self):
        response = requests.get(f"{self.base_url}/people/me", headers=self.headers)
        user_info = response.json()
        print(f"Display Name: {user_info.get('displayName', 'N/A')}")
        print(f"Nickname: {user_info.get('nickName', 'N/A')}")
        print(f"Emails: {', '.join(user_info.get('emails', []))}")
        input("Press Enter to go back to the menu...")

    def list_rooms(self):
        response = requests.get(f"{self.base_url}/rooms", headers=self.headers)
        rooms = response.json().get("items", [])
        for room in rooms[:5]:
            print(f"Room ID: {room.get('id', 'N/A')}")
            print(f"Room Title: {room.get('title', 'N/A')}")
            print(f"Date Created: {room.get('created', 'N/A')}")
            print(f"Last Activity: {room.get('lastActivity', 'N/A')}")
            print("-" * 30)
        input("Press Enter to go back to the menu...")

    def create_room(self):
        room_title = input("Enter the title for the new room: ")
        data = {"title": room_title}
        response = requests.post(f"{self.base_url}/rooms", headers=self.headers, json=data)
        if response.status_code == 200:
            print("Room created successfully!")
        else:
            print(f"Error: {response.status_code}")
        input("Press Enter to go back to the menu...")

    def send_message(self):
        response = requests.get(f"{self.base_url}/rooms", headers=self.headers)
        rooms = response.json().get("items", [])[:5]
        for i, room in enumerate(rooms):
            print(f"{i + 1}. {room.get('title', 'N/A')}")
        room_index = int(input("Choose a room to send a message to (1-5): ")) - 1
        room_id = rooms[room_index].get('id', None)
        if room_id:
            message = input("Enter the message to send: ")
            data = {"roomId": room_id, "text": message}
            response = requests.post(f"{self.base_url}/messages", headers=self.headers, json=data)
            if response.status_code == 200:
                print("Message sent successfully!")
            else:
                print(f"Error: {response.status_code}")
        else:
            print("Invalid room selection.")
        input("Press Enter to go back to the menu...")

    def main_menu(self):
        while True:
            print("Main Menu:")
            print("0. Test Connection")
            print("1. Display User Info")
            print("2. List Rooms")
            print("3. Create Room")
            print("4. Send Message to Room")
            print("5. Exit")
            choice = input("Enter your choice (0-5): ")

            if choice == "0":
                self.test_connection()
            elif choice == "1":
                self.display_user_info()
            elif choice == "2":
                self.list_rooms()
            elif choice == "3":
                self.create_room()
            elif choice == "4":
                self.send_message()
            elif choice == "5":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tool = WebexTroubleshootingTool()
    tool.main_menu()
