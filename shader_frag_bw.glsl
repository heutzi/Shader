#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;
out vec4 f_color;

float average(in vec3 v3){
    return (v3.r + v3.g + v3.b)/3;
}

void main() {
    vec3 sampled_col = texture(tex, uvs).rgb;
    float avg = average(sampled_col);
    f_color = vec4(vec3(avg),  1.0);
}