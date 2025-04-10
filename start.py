import os
import cv2
from ultralytics import YOLO
from detectWebsite import build_website_from_detections

images_dir = os.path.join('.', 'test_images1')
image_name = '162.png'
image_path = os.path.join(images_dir, image_name)

model_path = os.path.join('.', 'runs', 'detect',
                          'train6', 'weights', 'best.pt')
model = YOLO(model_path)


def detect_component(image_path):
    img = cv2.imread(image_path)

    height, width, channels = img.shape

    detection_results = model(img)[0]

    return detection_results, height, width

def generate_index_html():
    index_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Website Preview and Code</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      <style>
        body {
          font-family: Arial, sans-serif;
          padding: 20px;
        }
        #previewSection, #codeSection {
          display: none;
        }
        .active {
          display: block;
        }
      </style>
    </head>
    <body>

      <div class="container">
        <h1>AI Generated Website</h1>
        <div class="btn-group mb-4" role="group" aria-label="Toggle Preview and Code">
          <button type="button" class="btn btn-primary" id="showCodeBtn">Show Code</button>
          <button type="button" class="btn btn-primary" id="showPreviewBtn">Show Preview</button>
        </div>

        <!-- Code Section -->
        <div id="codeSection" class="active">
          <h3>Generated HTML Code</h3>
          <pre id="codeOutput"></pre>
        </div>

        <!-- Preview Section -->
        <div id="previewSection">
          <h3>Preview</h3>
          <iframe src="generated_website16.html" width="100%" height="600px"></iframe>
        </div>
      </div>

      <script>
        // Handle button clicks to toggle between code and preview
        const showCodeBtn = document.getElementById('showCodeBtn');
        const showPreviewBtn = document.getElementById('showPreviewBtn');
        const codeSection = document.getElementById('codeSection');
        const previewSection = document.getElementById('previewSection');
        const codeOutput = document.getElementById('codeOutput');

        // Load the generated HTML code into the code section
        fetch('generated_website16.html')
          .then(response => response.text())
          .then(data => {
            codeOutput.textContent = data;  // Show the HTML code in the code section
          });

        showCodeBtn.addEventListener('click', () => {
          codeSection.classList.add('active');
          previewSection.classList.remove('active');
        });

        showPreviewBtn.addEventListener('click', () => {
          previewSection.classList.add('active');
          codeSection.classList.remove('active');
        });
      </script>

    </body>
    </html>
    """
    
    # Write the content to the index.html file inside the 'generated' folder
    with open('generated/index.html', 'w') as file:
        file.write(index_html)
    print("index.html has been generated successfully!")



def main():
    detections, v_height, v_width = detect_component(image_path)
    html = build_website_from_detections(detections, v_width, v_height)

    # Specify the 'generated/' folder path
    generated_folder = os.path.join('.', 'generated')
    # Create the folder if it doesn't exist
    if not os.path.exists(generated_folder):
        os.makedirs(generated_folder)

    # Save the HTML file inside the 'generated/' folder
    html_file_path = os.path.join(generated_folder, "generated_website16.html")
    with open(html_file_path, "w") as f:
        f.write(html)


    generate_index_html()

    print(f"Website generated successfully and saved to {html_file_path}")




main()
