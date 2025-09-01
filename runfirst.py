# Run this script first to convert your music.mp3 to base64
import base64

def music_to_base64(music_file):
    """Convert music file to base64 string"""
    with open(music_file, 'rb') as f:
        music_data = f.read()
    
    base64_string = base64.b64encode(music_data).decode('utf-8')
    
    # Write to a Python file
    with open('music_data.py', 'w') as f:
        f.write(f'# Auto-generated music data\n')
        f.write(f'MUSIC_DATA = "{base64_string}"\n')
    
    print("Music converted to music_data.py")
    print(f"File size: {len(music_data)} bytes")
    print(f"Base64 size: {len(base64_string)} characters")

if __name__ == "__main__":
    music_to_base64("music.mp3")  # Change this to your music file name
