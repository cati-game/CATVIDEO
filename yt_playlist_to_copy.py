from yt_dlp import YoutubeDL

def generate_html_list(playlist_url, category_name, output_file=None, emoji="🎬"):
    ydl_opts = {
        'ignoreerrors': True,
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        print(f"Fetching playlist info for: {playlist_url} ...")
        info = ydl.extract_info(playlist_url, download=False)

        if 'entries' not in info:
            print("Error: Could not extract playlist entries.")
            return

        video_ids = [entry['id'] for entry in info['entries'] if entry]
        series_param = ",".join(video_ids)

        lines = []

        lines.append(f'<details id="cat-{category_name.lower().replace(" ", "-")}">')
        lines.append(f'  <summary>{emoji} {category_name}</summary>')
        lines.append('  <ul>')

        for video_id, entry in zip(video_ids, info['entries']):
            title = entry.get('title', 'Untitled')
            lines.append(
                f'    <li><input type="checkbox" data-id="{video_id}"> '
                f'<a href="video.html?vid={video_id}&series={series_param}">{title}</a></li>'
            )

        lines.append('  </ul>')
        lines.append('</details>')

        html_output = "\n".join(lines)

        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(html_output)
            print(f"\n✅ Saved HTML to: {output_file}")
        else:
            print("\n--- HTML Output ---\n")
            print(html_output)
            print("\n--- End of Output ---\n")


if __name__ == "__main__":
    print("🔥 YouTube Playlist to HTML Converter 🔥\n")

    playlist_url = input("Enter the YouTube playlist URL: ").strip()
    category_name = input("Enter the category name: ").strip()

    save_to_file = input("Save to txt file? (y/n): ").strip().lower()

    output_file = None
    if save_to_file == "y":
        output_file = input("Enter filename (e.g. output.txt): ").strip()

    if not playlist_url or not category_name:
        print("Error: Both playlist URL and category name are required.")
    else:
        generate_html_list(
            playlist_url,
            category_name,
            output_file=output_file
        )