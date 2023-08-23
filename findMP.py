from pynput import mouse

current_position = None

def on_click(x, y, button, pressed):
    global current_position

    if button == mouse.Button.right and pressed:
        current_position = (x, y)
        print(f"Mouse clicked at position: X = {x}, Y = {y}")

# Create a listener for mouse events
listener = mouse.Listener(on_click=on_click)
listener.start()

try:
    listener.join()
except KeyboardInterrupt:
    listener.stop()
    print("Mouse position monitoring stopped.")
