# Microservice A - Image-to-ASCII Color Converter

## Description
This microservice processes images and converts them into ASCII-compatible color representations.

## API Endpoint
- **URL:** `http://127.0.0.1:5000/process_image`
- **Method:** `POST`
- **Request Parameters:**
- `image` (file) - The image file to be processed.
- `mode` (integer) - Color selection mode:
- `0` represents the mean hue.
- `1` = Dominant color
- `2` = Top-left pixel
- `rows` (integer) - ASCII grid number of rows.
- `cols` (integer) - Number of columns in an ASCII grid.

## Illustrative Inquiry (Python)
```python
import requests

url = 'http://127.0.0.1:5000/process_image'
files = {'image': open('album_cover.jpg', 'rb')}
data = {'mode': 0, 'rows': 20, 'cols': 40}
response = requests.post(url, files=files, data=data)
color_grid = response.json()
display(color_grid)
```

## Response Format
- 2D JSON array of RGB tuples
```json
[[34, 56, 78],
[12, 34, 56],]]
[[98, 120, 140],
[76, 80, 90],
```

## Error Handling - If an invalid mode is provided, a default black color `(0,0,0)` will be returned.

- If image processing fails, it returns an error message.

## UML Sequence Diagram Go `uml_sequence_diagram.txt` 
## Mitigation Plan 
- **Colleague:** Katelyn 
- **Status:** Microservice is fully deployed. 
- **Access:** Clone from GitHub and run locally. 
- **In case of problems:** SMS contact; response within 12 hours. 
- **Deadline for reporting:** 3 days from integration. (Flexible)
- **Problems:** Make sure Flask server is running before sending requests.