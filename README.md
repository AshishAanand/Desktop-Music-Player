# 🎵 Music Player

Welcome to **Music Player**, a feature-rich and interactive application that allows you to play, manage, and enjoy your favorite music in an intuitive way! Built with Python and Tkinter, this app combines simplicity and functionality to create a seamless music experience.

---

## 📋 Features

- **Add Songs**: Easily add your favorite `.mp3` or `.wav` songs to the playlist from your computer.
- **Manage Playlist**: Automatically saves and loads your playlist so you never lose track of your songs.
- **Play Music**: Play your songs with one click and enjoy the tunes.
- **Pause & Resume**: Pause the current song and pick up where you left off anytime.
- **Next & Previous**: Switch between songs in the playlist effortlessly.
- **Stop Music**: Instantly stop the music playback when needed.
- **Error Handling**: Smooth handling of missing files or unsupported formats with user-friendly error messages.

---

## 🎛️ User Interface

The app offers a clean and interactive user interface with the following elements:
- **Playlist Box**: Displays your added songs.
- **Music Title**: Shows the currently playing song or status.
- **Controls**: Buttons for `Play`, `Pause`, `Next`, `Previous`, and `Add Music`.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/music-player.git
cd music-player
```
### 2. Install Requirements
Ensure you have Python installed on your system. Install the required libraries with:
```bash
pip install pygame
```
### 3. Run the Application
```bash
python music_player.py
```

---

# 🛠️ How to Use
### 1. Launch the App:
   - Open the application by running `music_player.py.`
### 2. Add Songs:

  - Click the "Add Music" button.
  - Select the .mp3 or .wav files from your computer.
  - Your selected files will be copied to the Musics directory and added to the playlist.
### 3. Play Music:

  - Select a song from the playlist or use the Play button to start playing the first song in the playlist.
### 4. Pause, Resume, Next, and Previous:

  - Control your playback using the corresponding buttons for a seamless experience.
### 5. Stop Music:

  - Stop the playback anytime by clicking the Stop button.

---

# 📂 Project Structure
- `music_player.py:` Main application file containing the code for the Music Player.
- `Musics/:` Directory where all added songs are stored.
- `music.json:` JSON file for saving and loading the playlist.

---

## 📌 Functionalities Explained

| **Feature**          | **Description**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| **Add Songs**         | Allows you to select songs from your device and adds them to the playlist.      |
| **Play Music**        | Plays the selected song or the first song in the playlist.                     |
| **Pause & Resume**    | Pause playback and resume from where you left off.                             |
| **Next & Previous**   | Navigate through your playlist with ease.                                      |
| **Stop Music**        | Stops the current playback immediately.                                        |
| **Persistent Playlist** | Automatically saves the playlist to `music.json` and reloads on app start.    |

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the project and submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## 🌟 Acknowledgments

Thanks to the open-source community for making projects like this possible.

---

### 🚨 Note:

- Ensure all songs are in `.mp3` or `.wav` format.
- Avoid removing the `Musics` directory or `music.json` file, as they are essential for functionality.

