import requests

def get_channel_details(channel_ids, api_key):
    channel_data = []
    for channel_id in channel_ids:
        url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={channel_id}&key={api_key}"
        response = requests.get(url)
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            item = data['items'][0]
            snippet = item['snippet']
            stats = item['statistics']
            channel_data.append({
                'Channel Name': snippet['title'],
                'Channel Description': snippet['description'],
                'Custom URL': snippet.get('customUrl', 'N/A'),
                'Profile Image': snippet['thumbnails']['high']['url'],
                'Subscribers': int(stats.get('subscriberCount', 0)),
                'Channel Thumbnail': snippet['thumbnails']['high']['url']
            })
    return channel_data

# Example usage
channel_ids = ["UCtxD0x6AuNNqdXO9Wp5GHew", "UCX6OQ3DkcsbYNE6H8uQQuVA"]  # MrBeast and Cristiano Ronaldo channels
api_key = 'YOUR_API_KEY'  # Replace with your API key
channel_details = get_channel_details(channel_ids, api_key)
print(channel_details)