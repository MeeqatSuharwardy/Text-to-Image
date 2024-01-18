from flask import Flask, request, render_template, jsonify
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import io
import base64

app = Flask(__name__)

# Load the model (consider loading it only once if it's resource-intensive)
device = "cpu"
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float32).to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-image', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    image_output = pipe(prompt).images[0]

    # Convert PIL image to base64 string
    buffered = io.BytesIO()
    image_output.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    return jsonify({'image': img_str})

if __name__ == '__main__':
    app.run(debug=True)
