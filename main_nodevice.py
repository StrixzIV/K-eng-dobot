import cv2
import image_utils

CLASS_NAMES = image_utils.load_classname('./model/labels.txt')

cap = cv2.VideoCapture(0)

while cap.isOpened():
	
	is_frame, frame = cap.read()

	if not is_frame:
		print("Failed to grab frame")
		break

	predicted_class, confidence = image_utils.predict(frame)

	if predicted_class is not None:

		class_name = CLASS_NAMES[predicted_class]
		cv2.putText(frame, f"Detected: {class_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
		
		print(f"Detected class: {class_name} with confidence: {confidence*100:.2f}%")

	else:
		cv2.putText(frame, "Low confidence", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
		print(f"Low confidence: {confidence*100:.2f}%")

	cv2.imshow('Frame', frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()