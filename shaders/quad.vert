#version 330 core

in vec2 vert;
in vec2 texcoord;
out vec2 uvs;


uniform vec2 window_size;

//uniform mat4 m_proj;
//uniform mat4 m_view;
//uniform mat4 m_model;

//uniform vec2 cam_position;

//uniform float self_rotation;
//uniform float camera_rotation;



void main() {
    uvs = texcoord;

    mat4 trasform = mat4(
        0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0
    );


    //trasform = translate * camera_z * projection * persepctive

    //gl_Position = vec4(vec4(vert, 0.0, 1.0)) / vec4(window_size / 2, 1.0, 1.0);
    gl_Position = vec4(vert, 0.0, 1.0);
    //gl_Position = m_proj * m_view * m_model * vec4(vert, 0.0, 1.0);
}
