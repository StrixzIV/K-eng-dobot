import cv2
import numpy as np
import tensorflow as tf

# Load the TensorFlow Lite model
interpreter = tf.lite.Interpreter(model_path="./model/model_unquant.tflite")
interpreter.allocate_tensors()

# Get input and output tensors
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def load_classname(path: str) -> list[str]:
    
    labels = []
    
    with open(path) as file:
        for line in file:
            _, label = line.strip().split(' ', 1)
            labels.append(label)
    
    return labels


def preprocess_image(image, input_shape):
	# Resize image to match model input size
	image = cv2.resize(image, (input_shape[1], input_shape[2]))
	# Normalize pixel values to [0, 1]
	image = image.astype(np.float32) / 255.0
	# Expand dimensions to match model input shape (add batch dimension)
	image = np.expand_dims(image, axis=0)
	return image

def predict(image: np.ndarray, minimum_confidence: float = 0.35) -> tuple[np.ndarray, float]:
	input_shape = input_details[0]['shape']
	image = preprocess_image(image, input_shape)

	# Debug: Print preprocessed image shape
	print(f"Preprocessed image shape: {image.shape}")

	interpreter.set_tensor(input_details[0]['index'], image)
	interpreter.invoke()
	output_data = interpreter.get_tensor(output_details[0]['index'])

	# Debug: Print raw output data and confidence scores
	confidence_scores = tf.nn.softmax(output_data[0])
	print(f"Raw output data: {output_data}")
	print(f"Confidence scores: {confidence_scores}")

	max_confidence = np.max(confidence_scores)
	predicted_class = np.argmax(confidence_scores)
	print(f"Max confidence: {max_confidence}, Predicted class: {predicted_class}")

	if max_confidence < minimum_confidence:
		return (None, max_confidence)
	
	return predicted_class, max_confidence