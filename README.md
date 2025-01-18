# Discord Music Bot 🎵

A feature-rich Discord bot built with Python and Discord.py to bring dynamic music playback functionality to your Discord server. This bot allows users to search for, queue, and play songs or playlists from YouTube directly into their voice channels.

---

## Features 🚀

- **YouTube Music Playback**: Stream high-quality audio from YouTube videos and playlists.
- **Queue Management**: Add, remove, and view songs in the playback queue.
- **Playback Controls**: Commands to play, pause, skip, and stop music.
- **Custom Command Prefix**: Change the bot's prefix for personalized interaction.
- **Robust Error Handling**: Handles invalid links, live streams, and unsupported formats gracefully.

---

## Commands 🛠️

### General Commands
- `/help`: Displays all available commands.
- `/prefix <new_prefix>`: Change the bot's command prefix.

### Music Commands
- `/play <keywords | URL>`: Search for a song or playlist on YouTube and play it in your current voice channel.
- `/queue`: Display the current song queue.
- `/pause`: Pause the current song or resume if already paused.
- `/resume`: Resume playback.
- `/skip`: Skip the current song.
- `/clear`: Clear the song queue and stop playback.
- `/stop`: Disconnect the bot from the voice channel.
- `/remove`: Remove the last song added to the queue.

---

## Installation 📦

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/discord-music-bot.git
   cd discord-music-bot
