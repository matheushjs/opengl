from glumpy import app, gloo, gl

vertex = """
    attribute vec2 position;
    attribute vec4 color;
    varying vec4 v_color;
    uniform float scale;
    void main(){
        gl_Position = vec4(scale*position, 0.0, 1.0);
        v_color = color;
    } """

fragment = """
    varying vec4 v_color;
    void main() { gl_FragColor = v_color; } """

window = app.Window()
quad = gloo.Program(vertex, fragment, count=4)
quad['position'] = (-1,+1), (+1,+1), (-1,-1), (+1,-1)
quad['color'] = (1,1,0,1), (1,0,0,1), (0,0,1,1), (0,1,0,1)

scale = 1
direction = 1

@window.event
def on_draw(dt):
    global scale, direction

    window.clear()
    quad['scale'] = scale
    quad.draw(gl.GL_TRIANGLE_STRIP)

    if scale <= 0 or scale >= 1:
        direction = -direction

    scale = scale + direction*0.05

app.run()
