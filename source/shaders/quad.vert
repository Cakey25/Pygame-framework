#version 330 core

in vec2 vert;
in vec2 tex_uv;

out vec2 uv;

void main() {
    uv = tex_uv;
    gl_Position = vec4(vert.x/1280, vert.y/720, 0.0, 1.0);
}

// add the window size as a uniform
