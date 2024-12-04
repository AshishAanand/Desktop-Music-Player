from tkinter import *
from tkinter import filedialog, messagebox
import pygame
import os
import json
import shutil


class MusicPlayer:
    def __init__(self, root):
        # Initialize GUI components and variables
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("800x600")
        self.root.minsize(700, 600)

        self.song_file = 'music.json'
        self.current_song_index = 0
        self.is_paused = False
        self.song_playlist = self.load_songs_to_playlist(self.song_file)

        self.setup_gui()
        self.initialize_mixer()

    def initialize_mixer(self):
        pygame.mixer.init()

    def load_songs_to_playlist(self, json_path):
        try:
            with open(json_path, "r") as file:
                data = json.load(file)
            return data.get("songs", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_playlist(self):
        with open(self.song_file, "w") as file:
            json.dump({"songs": self.song_playlist}, file, indent=4)

    def add_songs(self):
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
        destination_dir = os.path.abspath('Musics')

        # Ensure the destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        for file in files:
            try:
                title = os.path.basename(file)
                new_path = os.path.join(destination_dir, title)

                # Copy the file instead of renaming it
                if not os.path.exists(new_path):  # Avoid overwriting existing files
                    shutil.copy(file, new_path)

                self.song_playlist.append({"title": title, "file_path": new_path})
            except Exception as e:
                messagebox.showerror("Music Player", f"Error adding song: {e}")

        self.update_playlist_box()
        self.save_playlist()

    def update_playlist_box(self):
        self.playlist_box.delete(0, END)
        for song in self.song_playlist:
            self.playlist_box.insert(END, song["title"])

    def play_song(self):
        if not self.song_playlist:
            messagebox.showinfo("Music Player", "No songs in the playlist.")
            return

        if self.is_paused:
            self.resume_song()
            return

        try:
            song = self.song_playlist[self.current_song_index]
            pygame.mixer.music.load(song["file_path"])
            pygame.mixer.music.play()
            self.music_title.config(text=f"Playing: {song['title']}")
        except pygame.error as e:
            messagebox.showerror("Music Player", f"Error playing song: {e}")

    def pause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.is_paused = True
            self.music_title.config(text="Music Paused")
        else:
            messagebox.showinfo("Music Player", "No song is playing to pause.")

    def resume_song(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.music_title.config(text=f"Playing: {self.song_playlist[self.current_song_index]['title']}")


    def next_song(self):
        if self.current_song_index < len(self.song_playlist) - 1:
            self.current_song_index += 1
            self.play_song()
        else:
            messagebox.showinfo("Music Player", "No more songs in the playlist.")

    def previous_song(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
            self.play_song()
        else:
            messagebox.showinfo("Music Player", "No previous song in the playlist.")

    def setup_gui(self):
        self.playlist_box = Listbox(self.root, width=60, height=15)
        self.playlist_box.pack(pady=20)

        self.music_title = Label(self.root, text="No Song Playing", padx=15, pady=70, font=("Helvetica", 12))
        self.music_title.pack(pady=20)

        controls_frame = Frame(self.root)
        controls_frame.pack()

        Button(controls_frame, text="Previous Song", width=30, padx=15, pady=10, command=self.previous_song).grid(row=0, column=0, padx=20, pady=10)
        Button(controls_frame, text="Next Song", width=30, padx=15, pady=10, command=self.next_song).grid(row=0, column=1, padx=20, pady=10)
        Button(controls_frame, text="Pause", width=30, padx=15, pady=10, command=self.pause_song).grid(row=1, column=0, padx=20, pady=10)
        Button(controls_frame, text="Play", width=30, padx=15, pady=10, command=self.play_song).grid(row=1, column=1)

        Button(self.root, text="Add Music", width=30, padx=10, pady=10, command=self.add_songs).pack(pady=10)

        self.update_playlist_box()


# Run the application
if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()
