from yt_dlp import YoutubeDL

def generate_html_list(playlist_url, category_name, emoji="🎬"):
    ydl_opts = {
        'ignoreerrors': True,
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,  # only metadata, no video downloads
    }

    with YoutubeDL(ydl_opts) as ydl:
        print(f"Fetching playlist info for: {playlist_url} ...")
        info = ydl.extract_info(playlist_url, download=False)
        if 'entries' not in info:
            print("Error: Could not extract playlist entries.")
            return

        print("\n--- HTML Output ---\n")
        print(f'<details id="cat-{category_name.lower().replace(" ", "-")}">')
        print(f'  <summary>{emoji} {category_name}</summary>')
        print('  <ul>')

        for entry in info['entries']:
            if not entry:
                continue
            video_id = entry.get('id')
            title = entry.get('title', 'Untitled')
            print(f'    <li><input type="checkbox" data-id="{video_id}"> <a href="video.html?vid={video_id}">{title}</a></li>')

        print('  </ul>')
        print('</details>')
        print("\n--- End of Output ---\n")

if __name__ == "__main__":
    print("🔥 YouTube Playlist to HTML Converter 🔥\n")

    playlist_url = input("Enter the YouTube playlist URL: ").strip()
    category_name = input("Enter the category name (e.g. Chill Beats): ").strip()

    if not playlist_url or not category_name:
        print("Error: Both playlist URL and category name are required.")
    else:
        generate_html_list(playlist_url, category_name)
