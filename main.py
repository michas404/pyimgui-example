import glfw
import imgui
import webbrowser
from imgui.integrations.glfw import GlfwRenderer
from OpenGL.GL import glClear, GL_COLOR_BUFFER_BIT

def michas():
    if not glfw.init():
        return

    window = glfw.create_window(1200, 800, "pyimgui-example", None, None)
    glfw.make_context_current(window)

    imgui.create_context()
    io = imgui.get_io()
    io.fonts.add_font_from_file_ttf("font/ProggyClean.ttf", 26)

    renderer = GlfwRenderer(window)

    show_second_window = False
    show_third_window = False
    checkbox_1 = False
    checkbox_2 = True
    slider_1 = 0.5
    slider_2 = 0.8
    text_input_1 = "visit my site!"
    text_input_2 = "https://michas.lol/"

    while not glfw.window_should_close(window):
        glfw.poll_events()
        renderer.process_inputs()
        glClear(GL_COLOR_BUFFER_BIT)

        imgui.new_frame()

        imgui.set_next_window_size(800, 550, condition=imgui.FIRST_USE_EVER)
        imgui.begin("first window")
        imgui.text("cool pyimgui example with glfw")
        imgui.spacing()

        if imgui.begin_tab_bar("tabs"):
            if imgui.begin_tab_item("tab 1")[0]:
                if imgui.button("open second window"):
                    show_second_window = True
                if imgui.button("open third window"):
                    show_third_window = True
                if imgui.button("exit app"):
                    glfw.set_window_should_close(window, True)

                imgui.spacing()
                imgui.separator()
                imgui.spacing()

                _, checkbox_1 = imgui.checkbox("checkbox 1", checkbox_1)
                _, checkbox_2 = imgui.checkbox("checkbox 2", checkbox_2)

                imgui.spacing()
                imgui.separator()
                imgui.spacing()

                _, text_input_1 = imgui.input_text("text input 1", text_input_1, 256)
                _, text_input_2 = imgui.input_text("text input 2", text_input_2, 256)
                imgui.end_tab_item()

            if imgui.begin_tab_item("tab 2")[0]:
                imgui.text("slider controls")
                imgui.spacing()
                imgui.separator()
                imgui.spacing()

                _, slider_1 = imgui.slider_float("slider 1", slider_1, 0.0, 1.0)
                _, slider_2 = imgui.slider_float("slider 2", slider_2, 0.0, 1.0)
                imgui.end_tab_item()

            imgui.end_tab_bar()

        imgui.spacing()
        imgui.separator()
        imgui.spacing()

        if imgui.button("about me"):
            webbrowser.open("https://me.michas.lol/")

        imgui.text("docs will be posted here soon")
        imgui.same_line()
        if imgui.button("https://docs.michas.lol/"):
            webbrowser.open("https://docs.michas.lol/")

        imgui.end()

        if show_second_window:
            imgui.set_next_window_size(300, 200, condition=imgui.FIRST_USE_EVER)
            imgui.begin("second window")
            if imgui.button("close second window"):
                show_second_window = False
            imgui.spacing()
            imgui.text("sussyyyy bakaaa")
            imgui.end()

        if show_third_window:
            imgui.set_next_window_size(600, 250, condition=imgui.FIRST_USE_EVER)
            imgui.begin("third window", flags=imgui.WINDOW_NO_TITLE_BAR | imgui.WINDOW_NO_RESIZE)
            imgui.text("third window with custom title bar")
            imgui.same_line(imgui.get_window_width() - 30)
            if imgui.button("X"):
                show_third_window = False
            imgui.separator()
            imgui.spacing()
            imgui.text("this is the third window yayyy")
            imgui.end()

        imgui.render()
        renderer.render(imgui.get_draw_data())
        glfw.swap_buffers(window)

    renderer.shutdown()
    glfw.terminate()

if __name__ == "__main__":
    michas()