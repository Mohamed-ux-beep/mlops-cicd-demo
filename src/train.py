import time 
from src.utils import add_numbers

def train_model():
    print("Starting training ...")
    time.sleep(2)
    result = add_numbers(2, 3)
    print(f"Training Complete. Result: {result}")

if __name__=="__main__":
    train_model()
