# %%
# Import our dependencies
import torch
from training import FeedForwardNet, download_mnist_datasets

# %%
# defining a class mapping of our dataset
class_mapping = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

# %%
# implement our predict algorithm
def predict(model: FeedForwardNet, input, target, class_mapping):
    # set model in evaluation mode by calling eval() on from our model. To set it back to training mode you call train()
    model.eval() # eval() and train() method is are methods that act as a switch that you call on pytorch model to change how it behave (evaluate or train mode)
    
    # Lets us use context manager that comes with pytorch to disable gradient calculation. We only need gradient for training and no for evaluation.
    with torch.no_grad():
        # Get predictions: Tensor(1, 10) --> [ [0.1, 0.01, 0.2, 0.02, 0.6, ..., 0.03]] this is a sample of our prediction tensor
        predictions = model(input) # predictions here is a Tensor object with specific dimension. In our case here is 2 dimension tensor. First dimension is the number of input that we are passing to the model, in our case 1 input. And second dimension is number of classes that the model is set to predict, in our case 10. Tensor(1, 10)

        # Get predicted index: predicted index is the index of the highest value from our predictions
        predicted_index = predictions[0].argmax(0)

        # Get our predicted value by Mapping the predicted index to the relative class using our class_mapping
        predicted = class_mapping[predicted_index]

        # Get our expected value by Mapping the target index to the relative class using our class_mapping as well
        expected = class_mapping[target]

    # Return predicted and expected as tuple
    return predicted, expected

# %%
# Running inference
if __name__ == "__main__":
    # 1. Load back the model
    feed_forward_net = FeedForwardNet()
    state_dict = torch.load("feedforwardnet.pth")
    feed_forward_net.load_state_dict(state_dict)

    # 2. Load MNIST validation dataset
    _, validation_data = download_mnist_datasets()

    # 3. Get samples from the validation dataset for inference
    input, target = validation_data[0][0], validation_data[0][1]
    input2, target2 = validation_data[5][0], validation_data[5][1]

    # 4. Make Inference
    predicted, expected = predict(feed_forward_net, input, target, class_mapping)
    predicted2, expected2 = predict(feed_forward_net, input2, target2, class_mapping)

    print(f"1. Predicted: {predicted}, Expected: {expected}")
    print(f"2. Predicted: {predicted2}, Expected: {expected2}")

# %%
