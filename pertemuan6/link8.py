class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"Lagu '{title}' ditambahkan ke playlist.")

    def show_playlist(self):
        current = self.head
        if not current:
            print("Playlist kosong.")
            return
        print("Daftar Lagu:")
        while current:
            print(f"- {current.title}")
            current = current.next
        
    def play_all(self):
        current = self.head
        if not current:
            print("Playlist kosong.")
            return
        print("Memutar semua lagu:")
        while current:
            print(f"Memutar: {current.title}")
            current = current.next

playlist = Playlist()
playlist.add_song("On My Way")
playlist.add_song("Darkside")
playlist.add_song("Faded")

print()
playlist.show_playlist()
print()
playlist.play_all()