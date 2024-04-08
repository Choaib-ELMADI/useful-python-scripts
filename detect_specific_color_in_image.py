import cv2
import numpy as np
from PIL import Image

video_name = "boxes.mp4"
video_path = f"C:\\Users\\Choaib ELMADI\\Downloads\\D.I.F.Y\\Web Development\\Web Dev\\9) Python\\Python Useful Scripts\\Assets\\{ video_name }"

cap = cv2.VideoCapture(video_path)
frame_counter = 0

# color_to_detect = (241, 203, 123)  # SOFT BLUE
color_to_detect = (87, 233, 245)  # YELLOW
# color_to_detect = (10, 130, 255)  # ORANGE


def get_color_limits(color_to_detect):
    color = np.uint8([[color_to_detect]])  # type: ignore
    hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)  # type: ignore

    lower = hsv_color[0][0][0] - 10, 100, 100
    upper = hsv_color[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower, dtype=np.uint8)
    upper_limit = np.array(upper, dtype=np.uint8)

    return lower_limit, upper_limit


while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_color_limits(color_to_detect)
    cv2_mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)  # type: ignore
    pil_mask = Image.fromarray(cv2_mask)

    bbox = pil_mask.getbbox()
    if bbox is not None:
        cv2.rectangle(
            frame,
            (bbox[0], bbox[1]),
            (bbox[2], bbox[3]),
            (0, 0, 255),
            2,
        )

    frame_counter += 1
    if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    cv2.imshow("Frame", frame)
    # cv2.imshow("HSV Frame", hsv_frame)
    # cv2.imshow("Mask", cv2_mask)
    if cv2.waitKey(33) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
