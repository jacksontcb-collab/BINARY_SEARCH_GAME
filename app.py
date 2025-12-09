import gradio as gr
import random

def start_game():
    nums = sorted(random.sample(range(1, 101), 20))
    low, high = 0, len(nums) - 1
    mid = (low + high) // 2
    return (
        f"List: {nums}\n\nIs your number {nums[mid]}?",
        nums, low, high, mid
    )

def user_response(response, nums, low, high, mid):
        if response == "correct":
            return (
                f" Found it! The number was {nums[mid]}.",
                nums, low, high, mid
            )

    #logic for the game
        if low > high:
            return (" The number is not in the list!", nums, low, high, mid)

        if response == "higher":
            low = mid + 1
        else:  # lower
            high = mid - 1

        if low > high:
            return (" The number is not in the list!", nums, low, high, mid)

        mid = (low + high) // 2

        return (
            f"List: {nums}\n\nIs your number {nums[mid]}?",
            nums, low, high, mid
        )

#all the code for the buttons
with gr.Blocks() as demo:
    gr.Markdown("#  Binary Search Game")

    output = gr.Textbox(label="Game Status", lines=6)

    nums = gr.State()
    low = gr.State()
    high = gr.State()
    mid = gr.State()

    start_button = gr.Button("Start New Game")
    higher = gr.Button("Higher")
    lower = gr.Button("Lower")
    correct = gr.Button("Correct")

    start_button.click(start_game,
                       outputs=[output, nums, low, high, mid])

    higher.click(
        lambda nums, low, high, mid: user_response("higher", nums, low, high, mid),
        inputs=[nums, low, high, mid],
        outputs=[output, nums, low, high, mid],
    )

    lower.click(
        lambda nums, low, high, mid: user_response("lower", nums, low, high, mid),
        inputs=[nums, low, high, mid],
        outputs=[output, nums, low, high, mid],
    )

    correct.click(
        lambda nums, low, high, mid: user_response("correct", nums, low, high, mid),
        inputs=[nums, low, high, mid],
        outputs=[output, nums, low, high, mid],
    )

demo.launch()
