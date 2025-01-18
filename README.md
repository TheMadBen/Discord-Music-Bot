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
   git clone https://github.com/TheMadBen/discord-music-bot.git
   cd discord-music-bot

2. **Install FFmpeg (Full Build)**:
   ```bash
   FFmpeg is required for audio playback. Follow these steps to install the full build:
   
   1. Visit [Gyan.dev FFmpeg Builds](https://www.gyan.dev/ffmpeg/builds/).
   2. Under **"FFmpeg Builds"**, download the latest **"Full" build** in the zip file format (e.g., `ffmpeg-git-full.7z`).
   3. Extract the zip file to a directory of your choice, such as `C:\ffmpeg`.
   4. Navigate to the extracted directory and locate the `bin` folder (e.g., `C:\ffmpeg\bin`).
   5. Add the `bin` directory to your system's PATH environment variable:
      - Press `Win + R`, type `sysdm.cpl`, and press Enter.
      - Go to the **Advanced** tab and click **Environment Variables**.
      - In the **System Variables** section, find the `Path` variable and click **Edit**.
      - Click **New** and add the path to the FFmpeg `bin` folder (e.g., `C:\ffmpeg\bin`).
      - Save your changes and restart your terminal.
   6. Verify the installation by running:
      ```bash
      ffmpeg -version

3. **Set Up a Discord Bot and Get the Token**:
   ```bash
   1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   2. Click **New Application** and give your bot a name.
   3. Navigate to the **Bot** section and click **Add Bot**.
   4. Under **Token**:
      - Click **Reset Token** and copy the token.
      - Save the token in a file named `token.txt` in the project directory.
   5. Under **OAuth2** > **URL Generator**:
      - Select the following bot permissions:
        - `Read Messages/View Channels`
        - `Send Messages`
        - `Connect`
        - `Speak`
      - Copy the generated URL.
      - Paste the URL into your browser and follow the prompts to invite the bot to your Discord server.

