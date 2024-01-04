# %%
# imports
import torch;
from torch import nn;
from torch.utils.data import DataLoader;
from torchvision import datasets;
from torchvision.transforms import ToTensor;

# %%
# Neutral Network Class
class FeedForwardNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.flatten = nn.Flatten()
        self.dense_layers = nn.Sequential(
            nn.Linear(28*28, 256),
            nn.ReLU(),
            nn.Linear(256, 10)
        )
        self.softmax = nn.Softmax(dim=1)

    def forward(self, input_data):
        flattened_data = self.flatten(input_data)
        logits = self.dense_layers(flattened_data)
        predictions = self.softmax(logits)
        return predictions

# %%
# Downloading data function
def download_mnist_datasets():
    train_data = datasets.MNIST(
        root="data",
        train=True,
        download=True,
        transform=ToTensor()
    )
    validation_data = datasets.MNIST(
        root="data",
        train=False,
        download=True,
        transform=ToTensor()
    )

    return train_data, validation_data

# %%
# Function use to train one epoch with our NT
def train_one_epoch(model, data_loader, loss_fn, optimizer, device):
    for inputs, targets in data_loader:
        inputs, targets = inputs.to(device), targets.to(device)

        # Calculate loss
        predictions = model(inputs)
        loss = loss_fn(predictions, targets)
       
        # Backpropagate loss and update weights
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # print the loss for the last batch that we have
    print(f"Loss: {loss.item()}")

# %%
# Function use to train multiple epochs with our NT
def train(model, data_loader, loss_fn, optimizer, device, epochs):
    for i in range(epochs):
        print(f"Epoch {i+1}")
        train_one_epoch(model, data_loader, loss_fn, optimizer, device)
        print("--------------------")
    print("Training is done")

# %%
# Training our model
if __name__ == "__main__":
    # 1. Loading MNIST datasets
    train_data, _ = download_mnist_datasets()
    print('MNIST datasets downloaded.')

    # 2. Create a dataloader for our train dataset
    BATCH_SIZE = 128
    train_data_loader = DataLoader(dataset=train_data, batch_size=BATCH_SIZE)

    # 3 Build the model
    if(torch.cuda.is_available()):
        divice = "cuda"
    else:
        divice = "cpu"
    
    print(f"Using {divice} device")

    feed_forward_net = FeedForwardNet().to(divice) # This is our model

    # 4. Train the model
    EPOCHS = 10
    LEARNING_RATE = .001
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(
        feed_forward_net.parameters(),
        lr=LEARNING_RATE
    )

    train(model=feed_forward_net, data_loader=train_data_loader, loss_fn=loss_fn, optimizer=optimizer, device=divice, epochs=EPOCHS)

    # 5. Save a trained model

    torch.save(feed_forward_net.state_dict(), "feedforwardnet.pth")

    print("Model trained and stored at feedforwardnet.pth")
