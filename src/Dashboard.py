# import dependencies

from PIL import Image
import gradio as gr
import matplotlib.pyplot as plt
import numpy as np

# define a function to display the final result

def result_plot():
    ############ ToDo
    path = "TGI-Index-1.png"
    im = Image.open(path)
    im_array = np.asarray(im)
    fig, ax = plt.subplots()
    fig.set_size_inches(8,5)
    ax = plt.imshow(im_array)
    plt.show()
    return fig


# define a function to read the raw image

def read_image():
    ############ ToDo
    path = "map.png"
    im = Image.open(path)
    im_array = np.asarray(im)
    fig, ax = plt.subplots()
    fig.set_size_inches(8,5)
    ax = plt.imshow(im_array)
    plt.show()
    return fig
    
# create a dashboard

with gr.Blocks() as demo:
    with gr.Tab("Vineyard Map"):
        
        first_image_plot = gr.Plot()
        with gr.Row():
            upload_button = gr.UploadButton("Click to upload a your image")
            upload_button.upload(fn=read_image, inputs=None, outputs=first_image_plot)


        output_plot = gr.Plot()
        with gr.Row():
            calculate_button = gr.Button("Calculate")
            clear_button = gr.ClearButton()
        
        
        calculate_button.click(fn=result_plot, inputs=None, outputs=output_plot)
        clear_button.add([output_plot])
        clear_button.click()
            


demo.launch()
