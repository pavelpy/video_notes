"""
    Generate missing links
"""
import os
import youtube_dl

URL_TEMPLATE = 'https://youtu.be/{}'


def validate_name(name):
    return os.path.isdir(name) and len(name) == 11


def main():
    ydl_opts = {
        # 'forcedescription': True,
        'simulate': True,
        'quiet': True,
    }
    with open('./README.md', 'r') as f:
        readme_content = f.read()

    video_keys = (n for n in os.listdir(".") if validate_name(n))
    video_keys = (vk for vk in video_keys if vk not in readme_content)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for video_key in video_keys:
            url = URL_TEMPLATE.format(video_key)
            info = ydl.extract_info(url)
            title = info['title']
            dt = info['upload_date']
            year = slice(0, 4)
            month = slice(4, 6)
            day = slice(6, 8)
            date = r'\[{}-{}-{}\]'.format(dt[year], dt[month], dt[day])
            print(r'* [{date} {title}]({url}) \[[Краткое содержание](./{video_key}/README.md)\]'.format(**locals()))


if __name__ == '__main__':
    main()
