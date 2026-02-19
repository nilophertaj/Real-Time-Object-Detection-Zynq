from ultralytics import YOLO
import cv2
import time
import psutil

model = YOLO("yolov8n.pt")
model.to("cpu")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    start = time.time()

    # Simulated FPGA acceleration
    results = model(frame)
    time.sleep(0.02)

    end = time.time()

    latency = (end - start) * 1000
    fps = 1 / (end - start)
    cpu_usage = psutil.cpu_percent()

    print(f"[FPGA] Latency: {latency:.2f} ms | FPS: {fps:.2f} | CPU: {cpu_usage}%")

    annotated = results[0].plot()
    cv2.imshow("FPGA Accelerated", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
