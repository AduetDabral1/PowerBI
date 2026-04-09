import requests

def get_video_details(channel_ids, api_key, max_results=10):
    video_data = []
    for channel_id in channel_ids:
        # Get the channel name
        channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&key={api_key}"
        channel_response = requests.get(channel_url)
        channel_data = channel_response.json()
        channel_name = channel_data['items'][0]['snippet']['title']
        
        # Get the video details
        url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&order=date&maxResults={max_results}&key={api_key}"
        response = requests.get(url)
        data = response.json()
        
        for item in data.get('items', []):
            video_id = item['id'].get('videoId', 'N/A')
            if video_id != 'N/A':
                video_snippet = item['snippet']
                video_stats = get_video_statistics(video_id, api_key)
                video_data.append({
                    'Channel Name': channel_name,
                    'Video Title': video_snippet['title'],
                    'Video Description': video_snippet['description'],
                    'Video Thumbnail': video_snippet['thumbnails']['high']['url'],
                    'Video ID': video_id,
                    **video_stats
                })
    return video_data

def get_video_statistics(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    
    if 'items' in data and len(data['items']) > 0:
        stats = data['items'][0]['statistics']
        return {
            'Likes': int(stats.get('likeCount', 0)),
            'Comments': int(stats.get('commentCount', 0)),
            'Views': int(stats.get('viewCount', 0))
        }
    return {}

# Example usage
channel_ids = ["UCneyi-aYq4VIBYIAQgWmk_w", "UCzwCEE_PchiBULMnAJqhGVg", "UCnC8SAZzQiBGYVSKZ_S3y4Q", "UCOtQWL2z-tFbI-mgy_Rpdgg"]  
                    # Ranveer Allahbadia, Raj Shamani, Nikhil Kamath, Unfiltered by Samdish channels
api_key = 'YOUR_API_KEY'  # Replace with your API key
video_details = get_video_details(channel_ids, api_key)
print(video_details)