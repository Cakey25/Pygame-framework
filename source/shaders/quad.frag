#version 330 core

uniform sampler2D tex;

in vec2 uv;
out vec4 colour;

void main() {
    colour = vec4(texture(tex, uv).rgb, 1.0);
}
