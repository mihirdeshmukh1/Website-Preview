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

    print(f"Website generated successfully and saved to {html_file_path}")


main()
