#version 330 core

uniform sampler2D tex;
uniform float time;

in vec2 uvs;
out vec4 f_color;

void main() {
    vec3 sampled_col = texture(tex, uvs).rgb;
    float blue = sin(time*0.01)/4 + sampled_col.b;
    f_color = vec4(sampled_col.rg, blue,  1.0);
}