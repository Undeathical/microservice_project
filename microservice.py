from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import io

app = Flask(__name__)

def get_color(block, mode):
    pixels = np.array(block)
    if mode == 0:
        return tuple(np.mean(pixels.reshape(-1, 3), axis=0).astype(int))
    elif mode == 1:
        unique, counts = np.unique(pixels.reshape(-1, 3), axis=0, return_counts=True)
        return tuple(unique[np.argmax(counts)])
    elif mode == 2:
        return tuple(pixels[0, 0])
    return (0, 0, 0)

@app.route('/process_image', methods=['POST'])
@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        print("Received request...")

        file = request.files.get('image')
        if not file:
            print("No image provided.")
            return jsonify({"error": "No image provided"}), 400

        mode = request.form.get('mode', type=int)
        rows = request.form.get('rows', type=int)
        cols = request.form.get('cols', type=int)

        if mode is None or rows is None or cols is None:
            print("Invalid parameters.")
            return jsonify({"error": "Missing parameters"}), 400

        print(f"Processing image with mode={mode}, rows={rows}, cols={cols}")

        image = Image.open(io.BytesIO(file.read())).convert("RGB")
        img_width, img_height = image.size
        block_w, block_h = img_width // cols, img_height // rows
        color_grid = []

        for r in range(rows):
            row_colors = []
            for c in range(cols):
                left, upper = c * block_w, r * block_h
                right, lower = left + block_w, upper + block_h
                block = image.crop((left, upper, right, lower))
                row_colors.append(get_color(block, mode))
            color_grid.append(row_colors)

        # Convert NumPy int32 to Python int
        return jsonify([[tuple(map(int, color)) for color in row] for row in color_grid])

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
