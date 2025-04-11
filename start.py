import os
import cv2
import subprocess
import threading
from ultralytics import YOLO
from detectWebsite import build_website_from_detections


def start_monitoring():
    subprocess.Popen(['python', 'auto_commit.py'])


images_dir = os.path.join('.', 'test_images1')
image_name = '158.png'
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
    monitor_thread = threading.Thread(target=start_monitoring)
    monitor_thread.daemon = True
    monitor_thread.start()

    detections, v_height, v_width = detect_component(image_path)
    html = build_website_from_detections(detections, v_width, v_height)

    with open("generated_website16.html", "w") as f:
        f.write(html)

    print("Website generated successfully!")
    print("Changes will be automatically committed and pushed to the repository.")

    try:
        while True:
            user_input = input(
                "Press Enter to exit or type 'run' to regenerate the website: ").strip()
            if not user_input:
                break
            if user_input.lower() == 'run':
                detections, v_height, v_width = detect_component(image_path)
                html = build_website_from_detections(
                    detections, v_width, v_height)

                with open("generated_website16.html", "w") as f:
                    f.write(html)

                print("Website regenerated successfully!")
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
