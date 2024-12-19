# Python-catkin

# Beginner ROS Application: Publisher, Subscriber, and Custom Message

Welcome to my beginner ROS application! This project demonstrates the basics of creating a Publisher and Subscriber in ROS, as well as defining and using custom messages. 

---

## Features
1. **Basic Publisher-Subscriber Communication**:
   - The publisher sends a simple string message: `Hello, Sofonias`.
   - The subscriber receives the message and logs it.

2. **Custom Message Example**:
   - A custom message `Position` is created to share coordinates.
   - The publisher sends `x` and `y` values as position coordinates.
   - The subscriber processes and logs the received coordinates.

---

## Message Details

### `Position.msg`
```plaintext
string message
float32 x
float32 y
