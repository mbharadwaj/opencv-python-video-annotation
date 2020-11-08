import random
import time
import cv2

def __draw_label(img, text, pos, bg_color):
    font_face = cv2.FONT_HERSHEY_SIMPLEX
    scale = 0.8
    color = (0, 0, 0)
    thickness = cv2.FILLED
    margin = 2

    txt_size = cv2.getTextSize(text, font_face, scale, thickness)

    end_x = pos[0] + txt_size[0][0] + margin
    end_y = pos[1] - txt_size[0][1] - margin

    cv2.rectangle(img, pos, (end_x, end_y), bg_color, thickness)
    cv2.putText(img, text, pos, font_face, scale, color, 1, cv2.LINE_AA)

def main():
    video = cv2.VideoCapture('https://www.mediacollege.com/video-gallery/testclips/20051210-w50s.flv')
    video.set(cv2.CAP_PROP_FPS, 25)

    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = int(frame_count / fps)

    print('fps = ' + str(fps))
    print('number of frames = ' + str(frame_count))
    print('total duration (seconds) = ' + str(duration))

    mock_zipcode = random.randint(10000, 95000)
    start_time = random.randint(0, int(duration/2)) % mock_zipcode
    stop_time = random.randint(start_time+(int(duration/2)), duration) % mock_zipcode
    print(start_time, stop_time)

    label = f'zip {mock_zipcode} {stop_time - start_time}(s)'

    while True:
        success, frame = video.read()

        current_frame = int(video.get(cv2.CAP_PROP_POS_FRAMES))
        current_time = current_frame / fps

        if start_time < current_time < stop_time:
            __draw_label(frame, label, (20, 20), (255, 255, 255))

        cv2.imshow('video', frame)
        time.sleep(0.01)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    video.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
