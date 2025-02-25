import requests

def test_microservice(image_path, mode, rows, cols):
    url = 'http://127.0.0.1:5000/process_image'
    files = {'image': open(image_path, 'rb')}
    data = {'mode': mode, 'rows': rows, 'cols': cols}
    response = requests.post(url, files=files, data=data)
    return response.json()

if __name__ == '__main__':
    image_path = 'album_cover.jpg'  
    mode = 0  
    rows, cols = 20, 40  
    result = test_microservice(image_path, mode, rows, cols)
    print(result)
